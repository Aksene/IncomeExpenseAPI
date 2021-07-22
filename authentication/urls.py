from django.urls import path
from .views import RegisterView,VerifyEmail

# Calls the RegisterView method in the views.py class
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify')

]