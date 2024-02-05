from django.forms import ModelForm

from events.models import EventSignIn


class EventSignInForm(ModelForm):
    class Meta:
        model = EventSignIn
        fields = [
            "first_name",
            "last_name",
            "email",
            "newsletter_opt_in",
            "council_district",
            "zip_code",
        ]
        labels = {
            "council_district": "What Philadelphia City Council District do you live in?",
            "newsletter_opt_in": "Receive our Newsletter?",
        }
        help_texts = {
            "council_district": (
                "Philly Bike Action is organized by city council district. "
                "This information will help you connect with "
                "work we are doing in *your* community!"
            ),
            "zip_code": (
                "Optionally provide your Postal / Zip Code "
                "If you're unsure of your district, "
                "or just to help us get a better idea of "
                "the distribution of our attendees throughout the city."
            ),
        }
