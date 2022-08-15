from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
	path('register/', views.RegisterPage.as_view(), name='register'),
	path('login/', views.CustomLoginView.as_view(),name='login'),
	path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
	path('', views.Home.as_view(), name="home"),
	path('task/<int:pk>/', views.TaskDetail.as_view(), name="task"),
	path('create_task/', views.TaskCreate.as_view(), name='create_task'),
	path('task_update/<int:pk>/', views.TaskUpdate.as_view(), name="task_update"),
	path('delete_task/<int:pk>/', views.DeleteTask.as_view(), name='delete_task'),

]




# http://127.0.0.1:8000/