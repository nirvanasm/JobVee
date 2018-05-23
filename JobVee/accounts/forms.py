from django import forms
from django.contrib.auth.models import User, models
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from accounts.models import Profile

        
class UserRegistrationForm(UserCreationForm):

    #email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'})),
    #city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'City'})),
    #phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'})),
    city = forms.CharField()
    phone = forms.CharField()
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
        )



class EditUserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Profile
        fields = (
            'description',
            'city',
            'phone',
            'website',
        )