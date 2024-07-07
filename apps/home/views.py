from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'home/home.html')


def aboutus(request):
    return render(request,'home/about.html')


def service(request):
    return render(request,'home/service.html')


def department(request):
    return render(request,'home/department.html')


def contact(request):
    return render(request,'home/contact.html')


def appointment(request):
    return render(request,'home/appointment.html')

def success(request):
    context = {
        "bg": True
    }
    return render(request, 'success.html', context)