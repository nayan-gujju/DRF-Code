from django.urls import path
from phone.views import RegisterView, ExampleView
from phone.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('nayan', ExampleView.as_view(), name='nayan'), 
]       