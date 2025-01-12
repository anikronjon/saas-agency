from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Profile
from .forms import SignUpForm, ProfilePictureForm
from .custom_auth_backend import CustomAuthenticationBackend


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('account:signin')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = CustomAuthenticationBackend().authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account:profile')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid username/email or password.')

    return render(request, 'account/signin.html')


@login_required(login_url='account:signin')
def profile_view(request):
    user = request.user
    profile = Profile.objects.filter(user__exact=user)

    if request.method == 'POST':
        # Handle password change form
        password_form = PasswordChangeForm(user=user, data=request.POST)
        if password_form.is_valid():
            password_form.save()
            messages.success(request, 'Your password has been updated')
            return redirect('account:profile')

        # Handle profile picture upload
        profile_picture = request.FILES.get('picture')
        if profile:
            profile.picture = profile_picture
            profile.save()
        else:
            profile = Profile(user=user, picture=profile_picture)
            profile.save()
        messages.success(request, 'Profile picture updated.')
        return redirect('account:profile')
    else:
        password_form = PasswordChangeForm(user=user)

    return render(request, 'account/profile.html', {'user': user, 'profile': profile, 'password_form': password_form})
  

def signout_view(request):
    logout(request)
    return redirect('account:signin')
