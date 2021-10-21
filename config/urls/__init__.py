from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

admin.site.site_header = 'TDict Admin'
admin.site.site_title = 'TDict'

urlpatterns = [
    # Admin UI
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
