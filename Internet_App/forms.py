from django import forms
from .models import *


class signupForm(forms.ModelForm):
    class Meta:
        model=signupmaster
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=signupmaster
        fields=['firstname','lastname','gmail','password','city','state','mobile']

class complaint_form(forms.ModelForm):
    class Meta:
        model = complain
        fields = '__all__'

class complaint_update(forms.ModelForm):
    class Meta:
        model = complain
        fields = ['status']

class plan_form(forms.ModelForm):
    class Meta:
        model = plan
        fields = '__all__'

class Feedback_form(forms.ModelForm):
    class Meta:
        model = feedback
        fields = "__all__"