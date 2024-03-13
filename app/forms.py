from django import forms 

from app.models import *


class userform(forms.ModelForm):
    class Meta:

        model = User

        fields = ['username','first_name','last_name','password']

        widgets = {'password':forms.PasswordInput}



class userprofileform(forms.ModelForm):
    
    class Meta:
        model = userprofile
        fields = ['profile_pic']