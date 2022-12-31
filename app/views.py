from django.shortcuts import render

# Create your views here.
def bunny(request):
    d={'a':55,'b':501,'c':705}
    # d={'a':10,'b':20}
    return render(request,'bunny.html',d)