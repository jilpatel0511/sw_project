from django.shortcuts import render

# Create your views here.
def Index(req):
    return render(req,'index.html')

def Common(req):
    return render(req,'common.html')