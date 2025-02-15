from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, FormView

from accounts.forms import UserLoginForm, ContactForm

from .common import *  # noqa


class IndexView(TemplateView):

    template_name = "accounts/dev/index.html"


class UserLoginView(LoginView):

    form_class = UserLoginForm
    template_name = "accounts/dev/login.html"


class UserHomeView(LoginRequiredMixin, TemplateView):

    template_name = "accounts/dev/home.html"


class UserLogoutView(LogoutView):

    pass


class ContactFormView(FormView):

    form_class = ContactForm
    template_name = "accounts/dev/contact.html"
    success_url = "accounts:contact"

    def form_valid(self, form):
        form.send_email()
        super().form_valid(form)


class PrivacyPolicyView(TemplateView):

    template_name = "accounts/dev/privacy_policy.html"
