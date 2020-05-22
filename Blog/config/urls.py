from django.contrib import admin
from django.urls import path, include
import BlogApp.urls

# media 파일 사용을 위해 urls.py에서 import 해야 하는 코드
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogApp.views.home, name="home"),
    path('blog/', include(BlogApp.urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root = setting.MEDIA_ROOT)
