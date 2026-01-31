from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from app import views, customer, owner

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Include app-specific URLs
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
