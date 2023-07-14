from django.shortcuts import render
from django.http import HttpRequest , HttpResponse

# Create your views here.
def showContent(request):
	return render(request,'index.html')
