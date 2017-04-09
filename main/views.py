from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from .forms import UpdateProfile

from .admin import UserCreationForm


def home(request):
    return render(request, 'main/home.html', {})


def success(request):
    return render(request, 'main/success.html', dict())


def profile(request):
    if not request.user.is_authenticated:
        return redirect('home')
    else:
        context = dict()
        if request.method == 'POST':
            form = UpdateProfile(request.POST, instance=request.user)
            if form.is_valid():
                print('Form is valid')
                form.save()
                return redirect('success')
            else:
                print('Form is not valid')
                return redirect('home')
        else:
            context['form'] = UpdateProfile(instance=request.user)
        return render(request, 'main/update.html', context)


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
