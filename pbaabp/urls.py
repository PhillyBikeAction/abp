from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from sesame.views import LoginView
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

from pbaabp.admin import organizer_admin
from pbaabp.views import EmailLoginView

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("accounts/profile/", include("profiles.urls")),
    path("events/", include("events.urls")),
    path("release/", include("release.urls")),
    path("donations/", include("membership.urls")),
    path("campaigns/", include("campaigns.urls")),
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
    path("sesame/login/", LoginView.as_view(), name="sesame_login"),
    path("email/login/", EmailLoginView.as_view(), name="email_login"),
    path("maillink/", include("maillinks.urls")),
    path("rcos/", include("facets.urls")),
    path("projects/", include("projects.urls")),
    path("", include("pages.urls")),
    path("admin/", admin.site.urls),
    path("organizer/", organizer_admin.urls),
    path("cms/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("", include(wagtail_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
