from django.contrib.auth import forms as auth_forms
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class AuthenticationForm(auth_forms.AuthenticationForm):
    
    def confirm_login_allowed(self, user):
        super(AuthenticationForm,self).confirm_login_allowed(user)
        
        # if not user.is_verified:
        #     raise ValidationError("user is not verified")
        
        
class SignUpForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')  

    
    # For preventing duplicate emails
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("ایمیل قبلاً ثبت شده است.")
        return email

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            print("User will be saved.")
            user.save()
        return user
