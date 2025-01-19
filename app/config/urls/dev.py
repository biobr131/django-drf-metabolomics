from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("dev/", include("accounts.urls.dev")),
    path("dev/admin/", admin.site.urls),
    path("dev/silk/", include("silk.urls", namespace="silk")),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
