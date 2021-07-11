
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from authy.views import UserProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('authy.urls')),
    path('post/', include('post.urls')),
    path('post/', include('post.urls')),
    path('<username>/',UserProfile, name='profile'),
    path('<username>/saved',UserProfile, name='profilefavorites'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

