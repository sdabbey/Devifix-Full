from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('register/userpro', views.create_user_pro, name='register-userpro'),
    path('register/send_otp', views.send_otp, name="send_otp"),
    path('register/userpro/get-set-password-page', views.get_userpro_password_set_page, name="userpro-register-password"),
    path('login/userpro/', views.login_user_pro, name="login-userpro"),
    path('logout/', views.logout_user, name='logout'),
    
    path('register/userwork', views.create_user_work, name='register-userwork'),
    path('register/userwork/get-set-password-page', views.get_userwork_password_set_page, name="userwork-register-password"),
    path('login/userwork/', views.login_user_work, name="login-userwork"),
   
]
