from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("accounts.urls.prod")),
    path("admin/", admin.site.urls),
    path("silk/", include("silk.urls", namespace="silk")),
]
