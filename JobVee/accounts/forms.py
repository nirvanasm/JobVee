from django import forms
from django.contrib.auth.models import User, models
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from accounts.models import Profile

        
class UserRegistrationForm(UserCreationForm):
    city = forms.CharField()
    phone = forms.CharField()
    role = forms.CharField()
    
    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',    
            'first_name',
            'last_name',
            'email',
            'city',
            'phone',
            'role',
        )
        

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'description',
            'city',
            'phone',
            'website',
        )