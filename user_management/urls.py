from django.contrib import admin

from django.urls import re_path, include


from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
from users.views import CustomLoginView, ResetPasswordView, ChangePasswordView

from users.forms import LoginForm

urlpatterns = [
    re_path('admin/', admin.site.urls),

    re_path('', include('users.urls')),

    re_path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=LoginForm), name='login'),

    re_path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    #re_path('create/', auth_views.CreateView.as_view(template_name='users/create_meeting.html'), name='create'),

    re_path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    re_path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    re_path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    re_path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    re_path(r'^oauth/', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
