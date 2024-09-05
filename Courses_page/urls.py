from django.urls import path
from . import views

urlpatterns=[
    path('',views.Courses,name='courses'),
    path('thanks/',views.thanks,name='thanks'),
    path('download-app/', views.download_app, name='download_app'),  # Add this line

]