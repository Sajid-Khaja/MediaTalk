from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tweet.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Note the added trailing slash
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
