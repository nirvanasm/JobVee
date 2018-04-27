from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import UserRegistrationForm, EditProfileForm, EditUserForm
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def register(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            user.profile.city = form.cleaned_data.get('city')
            user.profile.phone = form.cleaned_data.get('phone')
            user.save()
            return redirect('/account')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'accounts/register.html',{'form': form})


def view_profile(request):
    args = { 'user': request.user }
    return render(request, 'accounts/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance = request.user)
        profile_form = EditProfileForm(request.POST, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/accounts/profile')
    else:
        user_form = EditUserForm(request.POST, instance = request.user)
        profile_form = EditProfileForm(request.POST, instance = request.user.profile)

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
