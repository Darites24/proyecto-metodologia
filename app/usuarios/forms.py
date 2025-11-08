from django import forms
from django.contrib.auth import authenticate, get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned = super().clean()
        username = cleaned.get('username')
        password = cleaned.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError('Credenciales inválidas')
            cleaned['user'] = user
        return cleaned
    

User = get_user_model()

class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
       email = self.cleaned_data.get('email')
       if email and User.objects.filter(email__iexact=email).exists():
           raise forms.ValidationError('Ya existe un usuario con ese correo')
       return email
    
    def clean_password(self):
        p1 = self.cleaned_data.get('password1')
        p2 = self.cleaned_data.get('password2')
        if not p1 or p2 or p1 != p2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return p2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
