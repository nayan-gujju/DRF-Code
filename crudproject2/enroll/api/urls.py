from django.urls import path, include
from rest_framework.routers import DefaultRouter
from enroll.api import views

router = DefaultRouter()

router.register('crud', views.UserApi, basename='user')
urlpatterns = [
    path('', include(router.urls))
]