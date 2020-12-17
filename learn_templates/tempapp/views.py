from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request,'index.html')

def relative(request):
  return render(request,'relative_url.html')

def others(request):
  return render(request,'other.html')