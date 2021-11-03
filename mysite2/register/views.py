
from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.
def register(response):
    if response.method=="POST":
        #take the details from the page
        form = RegisterForm(response.POST)
        #check validation and save if is does validate in the database
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response,"register/register.html",{"form":form})
