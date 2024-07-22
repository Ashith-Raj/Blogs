from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Thalathoor/home.html')
# def home2(request):
#     return render(request,'Thalathoor/home2.html')