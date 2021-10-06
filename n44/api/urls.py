from django.urls import path
from . import views
urlpatterns = [
    path('studentapi/', views.StudentList.as_view(), name='student_api'),
    path('studentdetail/<int:pk>', views.StudentDetail.as_view(), name='student_list'),
    path('student-delete/<int:pk>', views.StudentDelete.as_view(), name='student_delete'),
    path('userapi/', views.UserList.as_view(), name='user_api'),
    path('userdetail/<int:pk>', views.UserDetail.as_view(), name='user_list'),
    path('user-delete/<int:pk>', views.UserDelete.as_view(), name='user_delete'),
]