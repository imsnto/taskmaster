from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import register 

urlpatterns = [
    path('login/', LoginView.as_view(template_name="accounts/login.html", next_page="/tasks/"), name="login"),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')

]