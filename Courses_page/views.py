from django.shortcuts import render
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
import os

@login_required
def Courses(request):
    return render(request,'html/Courses.html')

@login_required
def download_app(request):

    file_path = os.path.join('static', 'App.zip') 
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    return response
@login_required
def thanks(request):
    return render(request,'html/thanks.html')