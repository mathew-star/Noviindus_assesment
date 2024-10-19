# user/urls.py
from django.urls import path
from .views import register, CustomLoginView,HomePageView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login', template_name=None), name='logout'),
    path('', HomePageView.as_view(), name='home'),
]
