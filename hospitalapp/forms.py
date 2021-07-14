from .models import *
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation

class UserCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    name = forms.CharField(label='Name', widget=forms.TextInput)
    username = forms.CharField(label='Username', widget=forms.TextInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    address = forms.CharField(label='Address', widget=forms.Textarea(attrs={'rows': 4}))
    CHOICES = [('Male', 'male'), ('Female', 'female'), ('Other', 'other')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    age = forms.IntegerField(label='Age', widget=forms.NumberInput)
    phone_number = forms.CharField(label='Phone Number', widget=forms.TextInput)

    class Meta:
        model = Register
        fields = ('name','username','email','address','gender','age','phone_number')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
    
    def _post_clean(self):
        super()._post_clean()
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"