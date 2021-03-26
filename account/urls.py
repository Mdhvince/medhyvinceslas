from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path("", views.index, name="index_account"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),


    # 1 - form: ask for reseting the password
    # 2 - Success message page : email sent
    # 3 - Link to clique inside the email
    # 4 - form: reset the password
    path("reset_password",
         auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"),
         name="reset_password"
    ),
    path("reset_password_sent",
         auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"),
         name="password_reset_done"
    ),
    path("reset/<uidb64>/<token>",
         auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"),
         name="password_reset_confirm"
    ),
    path("reset_password_complete",
         auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"),
         name="password_reset_complete"),
]