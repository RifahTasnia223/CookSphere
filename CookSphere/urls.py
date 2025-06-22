from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/social/', permanent=False)),
    path('accounts/profile/', RedirectView.as_view(url='/social/profile/', permanent=False)),
    path('admin/', admin.site.urls),
    path('social/', include('social.urls')),  # Include URLs from the social app
    path('accounts/', include('allauth.urls')),  # Django Allauth routes
]

# Media file handling during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)