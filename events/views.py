import datetime
import uuid

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils import timezone

from events.forms import EventSignInForm
from events.models import EventSignIn, ScheduledEvent


def _fetch_event_by_slug_or_id(event_slug_or_id):
    try:
        uuid.UUID(event_slug_or_id)
        event_by_id = ScheduledEvent.objects.filter(id=event_slug_or_id).first()
    except ValueError:
        event_by_id = None
    event_by_slug = ScheduledEvent.objects.filter(wordpress_slug=event_slug_or_id).first()

    if event_by_id is not None:
        return event_by_id
    elif event_by_slug is not None:
        return event_by_slug
    else:
        return None


def event_view(request, event_slug_or_id):
    event = _fetch_event_by_slug_or_id(event_slug_or_id)
    if event is None:
        raise Http404
    html = "<html><body>%s</body></html>" % str(event)
    return HttpResponse(html)


def event_signin(request, event_slug_or_id):
    event = _fetch_event_by_slug_or_id(event_slug_or_id)
    if event is None:
        raise Http404
    if request.method == "POST":
        form = EventSignInForm(request.POST)
        if form.is_valid():
            # Check for a previous submission
            existing_signin = EventSignIn.objects.filter(
                event=event, email__iexact=form.instance.email
            ).first()
            if existing_signin is not None:
                existing_signin.first_name = form.instance.first_name
                existing_signin.last_name = form.instance.last_name
                existing_signin.council_district = form.instance.council_district
                existing_signin.zip_code = form.instance.zip_code
                existing_signin.newsletter_opt_in = form.instance.newsletter_opt_in
                existing_signin.save()
            else:
                form.instance.event = event
                form.save()

            if request.GET.get("kiosk", False):
                return redirect(
                    "event_signin_kiosk_postroll", event_slug_or_id=event.wordpress_slug
                )
            else:
                return HttpResponseRedirect("https://bikeaction.org")
    elif timezone.now() > event.start_datetime + datetime.timedelta(days=1):
        return HttpResponseRedirect("https://bikeaction.org")
    else:
        form = EventSignInForm()

    return render(request, "signin.html", context={"event": event, "form": form})


def event_signin_kiosk_postroll(request, event_slug_or_id):
    event = _fetch_event_by_slug_or_id(event_slug_or_id)
    if event is None:
        raise Http404
    return render(request, "signin-kiosk-postroll.html", context={"event": event})
