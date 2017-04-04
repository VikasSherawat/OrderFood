from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf

from .admin import UserCreationForm


def home(request):
    return render(request, 'main/home.html', {})


def success(request):
    return render(request, 'main/success.html', dict())


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')

    context = {}
    context.update(csrf(request))
    context['form'] = UserCreationForm()

    return render(request, 'registration/register.html', context)
