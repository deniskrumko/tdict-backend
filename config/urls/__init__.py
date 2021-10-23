from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

from apps.dictionary.api import router as dictionary_router

admin.site.site_header = 'TDict Admin'
admin.site.site_title = 'TDict'


urlpatterns = [
    # Admin UI
    path('', RedirectView.as_view(url='admin/')),
    path('admin/', admin.site.urls),

    # API
    path('api/', include(dictionary_router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
