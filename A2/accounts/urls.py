from django.urls import path
from accounts import views
urlpatterns = [
    path('',views.SignUpView.as_view(), name= 'signup' ),
    path('login/', views.user_login, name='login'),
    path('profile/', views.user_profile, name='profile'),
    path('profileview/', views.user_profile_view, name='profileview'),
    path('logout/', views.user_logout, name='logout'),
]