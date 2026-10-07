from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from media.views import upload_media, gallery, delete_media, edit_media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_media, name='upload_media'),
    path('gallery/', gallery, name='gallery'),
    path('delete/<int:id>/', delete_media, name='delete_media'),
    path('edit/<int:id>/', edit_media, name='edit_media'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)