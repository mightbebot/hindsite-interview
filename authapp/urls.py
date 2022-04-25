from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)

from .views import edit, dashboard, TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView, TaskReorder, RegisterPage

app_name = 'authapp'

urlpatterns = [
    path('register/', RegisterPage.as_view(), name='register'),
    path('edit/', edit, name='edit'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='authapp/logged_out.html'), name='logout'),
    
    path('password_change/', PasswordChangeView.as_view(
        template_name='authapp/password_change_form.html'), name='password_change'),

    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='authapp/password_change_done.html'),
         name='password_change_done'),
    
    path('password_reset/', PasswordResetView.as_view(
        template_name='authapp/password_reset_form.html',
        email_template_name='authapp/password_reset_email.html',
        success_url=reverse_lazy('authapp:password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='authapp/password_reset_done.html'), name='password_reset_done'),
        
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='authapp/password_reset_complete.html'), name='password_reset_complete'),
    
    
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(
        success_url=reverse_lazy('authapp:tasks')), name='task_create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(
        success_url=reverse_lazy('authapp:tasks')), name='task_update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(
        success_url=reverse_lazy('authapp:tasks')), name='task_delete'),
    path('task-reorder/', TaskReorder.as_view(), name='task-reorder'),

]
