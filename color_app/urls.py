from django.urls import path
from . import views 
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/register/', views.RegisterView.as_view(), name='register'),
    path('api/login/', views.LoginView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/color/', views.ColorChangeView.as_view(), name='color_change'),
    path('api/user/', views.UserInfoView.as_view(), name='user_info'),
]
