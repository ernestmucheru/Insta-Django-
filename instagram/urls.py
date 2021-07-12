
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from authy.views import UserProfile,follow

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('authy.urls')),
    path('direct/', include('direct.urls')),
    path('post/', include('post.urls')),
    path('notifications/', include('notifications.urls')),
    path('<username>/',UserProfile, name='profile'),
    path('<username>/saved',UserProfile, name='profilefavorites'),
    path('<username>/follow/<option>', follow , name ='follow'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

