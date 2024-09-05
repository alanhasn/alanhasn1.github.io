from django.shortcuts import render , HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def about(request):
    return render(request,'html/about.html')