from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .forms import UserForm

def register(response):
    if response.method == "POST":
	    form = UserForm(response.POST)
	    if form.is_valid():
	        form.save()
	        return redirect("home")
    else:
	    form = UserForm()

    return render(response, "users/register.html", {"form":form})