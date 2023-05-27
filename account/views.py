from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm


# Registration View
def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse('You signup successfully.')
    else:
        form = RegistrationForm()
    return render(request, 'account/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponse(f'You login sucessfully: {request.user}')
    else:
        form = AuthenticationForm()
    return render(request, 'account/signin.html', {'form': form})
