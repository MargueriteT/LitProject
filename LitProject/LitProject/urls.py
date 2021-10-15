from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(
        template_name='users/login.html', redirect_authenticated_user=True),
         name='login'),
    path('register/', user_views.register, name='register'),
    path('home/', include('blog.urls')),
    path('userfollows-home/', include('userfollows.urls')),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
