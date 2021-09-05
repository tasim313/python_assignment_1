from django.urls import path

from . import views

app_name = 'student_info'

urlpatterns = [
    # path('', views.StudentForm, name='student_insert'),
    path('', views.StudentInfo.as_view(), name='student_info'),
    path('list/', views.ListPage.as_view(), name='student_list'),
    path('edit/<pk>/', views.EditPage.as_view(), name='student_edit'),
    path('delete/<pk>', views.DeletePage.as_view(), name='delete'),
    path('details/<pk>/', views.StudentDetail.as_view(), name='details'),
]
