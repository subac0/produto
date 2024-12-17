from django import forms
from .models import Produto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'quantidade', 'preco', 'imagem']

class CadastroForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, min_length=6)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True, min_length=6)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")
        return cleaned_data
    
    def save(self):
         username = self.cleaned_data.get("username")
         email = self.cleaned_data.get("email")
         password = self.cleaned_data.get("password")
         
         user = User.objects.create_user(username=username, email=email, password=password)
         return user