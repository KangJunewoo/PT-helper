from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin - handling DBs
    path('admin/', admin.site.urls),
    
    # general - index, main, help
    path('/', include('general.urls')),
    
    # presentation - add, show, make
    # path('presentation/', include('presentation.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)