from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # app path
    path('', include('listings.urls')),
    path('joblist/', include('joblist.urls')),
    path('startup/', include('startup.urls')),    
    path('profile/', include('profiles_api.urls')),
    
    # rest framework path
    path('api/startup/', include('startup.api.urls', 'startup_api')),
    path('api/job/', include('joblist.api.urls', 'job_api')),    
    path('api/profile', include('profiles_api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
