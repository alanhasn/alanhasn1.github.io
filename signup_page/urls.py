from django.urls import path
from .views import SignUp,logout

urlpatterns=[
    path('',SignUp,name='signup'),
    path('logout/',logout,name='logout')
]