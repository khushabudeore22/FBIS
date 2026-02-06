# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from SMSapp.models import logindata

# Create your views here.
# def about(request):
#     return HttpResponse("Hello I am INDEX Page")

def index(request):
    return render(request, "SMSapp/index.html")

# def about(request):
#     return render(request, "SMSapp/templates/SMSapp/about.html")

def login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        logindata.objects.create(
            name=name,
            email=email
        )

        return redirect("login")  

    return render(request, "SMSapp/login.html")
