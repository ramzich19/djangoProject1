from django.urls import path
from django.conf.urls import  url
from .views import signin, signup, signout, edit
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^auth/password/change/$', auth_views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^auth/password/change/done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^auth/password/reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^auth/password/reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^auth/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),

    url(r'^auth/password/reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='signout'),
    path('profile/', edit, name='profile'),

]
