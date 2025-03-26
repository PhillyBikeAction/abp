from django import forms
from django.utils.translation import gettext_lazy as _
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Invisible


class EmailLoginForm(forms.Form):
    email = forms.EmailField(
        help_text="The email address you used to sign up for your Philly Bike Action Account"
    )


class NewsletterSignupForm(forms.Form):

    def __init__(self, *args, form_name=None, **kwargs):
        self.auto_id = f"{form_name}_%s"
        super().__init__(*args, **kwargs)

    newsletter_signup_captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)

    newsletter_signup_name = forms.CharField(
        required=True,
        label=_("Your Name"),
        widget=forms.TextInput(attrs={"hx-validate": "true", "placeholder": "Your Name"}),
    )
    newsletter_signup_email = forms.EmailField(
        label=_("Email"),
        widget=forms.TextInput(
            attrs={"hx-validate": "true", "placeholder": "Email", "type": "email"}
        ),
    )
