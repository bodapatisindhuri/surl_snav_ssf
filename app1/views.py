from django.shortcuts import render

# Create your views here.


def kind(request):
    return render(request,'kind.html')
def peace(request):
    return render(request,'peace.html')