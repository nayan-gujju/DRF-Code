from django.urls import path
from .import views
urlpatterns = [
    path('student-registration/', views.student_registration, name='student_reg'),
    path('user-registration/', views.user_registration, name='user_reg'),
]