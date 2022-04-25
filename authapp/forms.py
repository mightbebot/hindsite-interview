from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Employee, Organisation


class UserEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email', 'organisation')



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    organisation = forms.CharField(label='Your Organisation', max_length=100, required=True)

    class Meta:
        model = Employee
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.organisation = Organisation.objects.create(name=self.cleaned_data['organisation'], country='australia', language='english')
        if commit:
            user.save()
        return user


class PositionForm(forms.Form):
    position = forms.CharField()

