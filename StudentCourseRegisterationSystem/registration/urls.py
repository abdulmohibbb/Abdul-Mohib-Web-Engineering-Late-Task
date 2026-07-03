from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .forms import StudentLoginForm
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html', authentication_form=StudentLoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('courses/', views.course_list, name='courses'),
    path('courses/enroll/<int:course_id>/', views.enroll_course, name='enroll_course'),
    path('courses/drop/<int:enrollment_id>/', views.drop_course, name='drop_course'),
]
