from django import forms
from process.models import *
import random
from process.utils import sendTextMessage,sendEmail

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    def clean_otp(self):
        cno = self.cleaned_data['contact']
        email = self.cleaned_data['email']
        otp = random.randint(100000,999999)
        message = 'Welcome to Resume Management System, Thanks for your Registration...Your OTP is '+str(otp)
        sendTextMessage(message,cno)
        sendEmail(email,message)
        return otp

    class Meta:
        model = RegistrationModel
        exclude = ('status',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ('pno',)
