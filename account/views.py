from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm
from .custom_auth_backend import CustomAuthenticationBackend


# Registration View
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse('You signup successfully.')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = CustomAuthenticationBackend().authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse(f'Login: {request.user}')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid username/email or password.')

    return render(request, 'account/signin.html')
