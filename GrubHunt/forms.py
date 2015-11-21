from django import forms
from django.contrib.auth.models import User
from GrubHunt.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

# This is what I tried previously. Ignore it.
# class EditProfileForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = ['username', 'email', ]
    
#     def __unit__(self, user, *args, **kwargs):
#         self.user = user.get_profile()

