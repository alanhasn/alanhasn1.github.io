from django.urls import path
from .views import Login, Forgot_Password

urlpatterns=[
    path('',Login,name='login'),
    path('forgot_password',Forgot_Password,name='forgot')

]