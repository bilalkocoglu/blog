from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Kullanici Adi')
    password = forms.CharField(max_length=100, label='Sifre', widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Giris Bilgileri Hatali !')

        return super(LoginForm, self).clean()

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, label='Kullanici Adi')
    password1 = forms.CharField(max_length=100, label='Sifre', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Sifre Dogrulama', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
        ]

    def clean_password2(self):
        passrowd1 = self.cleaned_data.get('password1')
        passrowd2 = self.cleaned_data.get('password2')

        if passrowd1 and passrowd2 and passrowd1 != passrowd2:
            raise forms.ValidationError('Sifreler birbiriyle uyusmuyor.')
        return passrowd2