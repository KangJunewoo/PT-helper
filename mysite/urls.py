from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
  # 계정
    path('account/', include('accounts.urls')),
    # 발표
    path('presentation/', include('presentation.urls')),
    #여기부터 url 입력 ㄱㄱ
    path('', include('PT_helper_web.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)