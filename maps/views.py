from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render, redirect
from django.forms import inlineformset_factory
from accounts.models import Role
from mdi.models import Organization, SocialNetwork
from formtools.wizard.views import SessionWizardView
from .forms import BranchForm, RoleForm, BasicInfoForm, DetailedInfoForm, ContactInfoForm, UserSocialNetworkFormSet
from dal import autocomplete


# Inline Formset for SocialNetworks.
def manage_socialnetworks(request, user_id):
    user = get_user_model().objects.get(pk=user_id)
    SocialNetworkInlineFormSet = inlineformset_factory(get_user_model, SocialNetwork, fields=('title',))
    if request.method == "POST":
        formset = SocialNetworkInlineFormSet(request.POST, request.FILES, instance=user)
        if formset.is_valid():
            # Do something. Should generally end with a redirect. For example:
            return HttpResponseRedirect(user.get_absolute_url())
    else:
        formset = SocialNetworkInlineFormSet(instance=user)
    return render(request, 'manage_books.html', {'formset': formset})


# Profile flow
# This trivially branches to either the Organization or Individual Profile `django-formtools` wizard.
@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        if request.POST['type'] == 'org':
            return redirect('organization-profile')
        else:
            return redirect('individual-profile')

    else:
        profile_type_form = BranchForm()
        return render(request, 'maps/profiles/branch.html', {
            'profile_type_form': profile_type_form,
            'title': 'Organisation or Individual?'
        })


# This operates the Individual Profile wizard via `django-formtools`.
INDIVIDUAL_FORMS = [
    ('role', RoleForm),
    ('basic_info', BasicInfoForm),
    ('detailed_info', DetailedInfoForm),
    ('contact_info', ContactInfoForm),
    ('social_networks', UserSocialNetworkFormSet),
]

INDIVIDUAL_TEMPLATES = {
    'role': 'maps/profiles/individual/role.html',
    'basic_info': 'maps/profiles/individual/basic_info.html',
    'detailed_info': 'maps/profiles/individual/detailed_info.html',
    'contact_info': 'maps/profiles/individual/contact_info.html',
    'social_networks': 'maps/profiles/individual/social_networks.html',
}


class IndividualProfileWizard(LoginRequiredMixin, SessionWizardView):
    def get_template_names(self):
        return [INDIVIDUAL_TEMPLATES[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form=form, **kwargs)

        if self.steps.current == 'detailed_info':
            role = self.get_cleaned_data_for_step('role')
            print('role.cleaned {}'.format(role))
            # Display `Services` if Individual is in Roles other than `Coop Founder` or `Coop Member`.
            for r in role:
                if r not in ['Coop Founder', 'Coop Member']:
                    context.update({'display_services': True})
                if r == 'Service Provider':
                    context.update({'display_coops_worked_with': True})
                if r == 'Researcher':
                    context.update({
                        'display_field_of_study': True,
                        'display_affiliation': True,
                        'display_projects': True
                    })
        return context

    # Attempt to solve SocialNetwork problem on profile pages.
    def get_form_initial(self, step):
        initial = []
        if step == 'social_networks':
            socialnetworks = SocialNetwork.objects.all()
            for index, sn in enumerate(socialnetworks):
                initial.append({
                    'socialnetwork' : sn,
                    'name': sn.name,
                    'hint' : sn.hint,
                })
            # print(initial)
        return self.initial_dict.get('social_networks', initial)

    def done(self, form_list, form_dict, **kwargs):
        form_dict = self.get_all_cleaned_data()
        user = self.request.user
        print('\n  current user: {}\n'.format(user))
        print('\n  form_list: {}\n'.format(form_list))
        print('\n  form_dict: {}\n'.format(form_dict))
        for k, v in form_dict.items():
            if k not in ['role', 'languages', 'services', 'challenges', 'formset-social_networks', ]:
                setattr(user, k, v)
        user.save()
        user.languages.set(form_dict['languages'])
        user.services.set(form_dict['services'])
        user.challenges.set(form_dict['challenges'])
        for sn in form_dict['formset-social_networks']:
            print('sn: {}'.format(sn))
            
            user.socialnetworks.set(sn)
        user.role.set(form_dict['role'])
        return HttpResponseRedirect('individual_detail')


# Autocomplete views for profile creation.
class OrganizationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # if not self.request.user.is_authenticated():
        #     return Organization.objects.none()

        qs = Organization.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


def index(request):
    template = loader.get_template('maps/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


# Organization
def organization_detail(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    context = {
    }
    return render(request, 'maps/organization_detail.html', {'organization': organization})


# Individual
def individual_detail(request, user_id):
    user = get_object_or_404(settings.AUTH_USER_MODEL, pk=user_id)
    context = {
    }
    return render(request, 'maps/individual_detail.html', {'individual': user})


# Static pages
class PrivacyPolicyView(TemplateView):
    template_name = "maps/privacy_policy.html"


class TermsOfServiceView(TemplateView):
    template_name = "maps/terms_of_service.html"


