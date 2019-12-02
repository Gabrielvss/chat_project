from django.forms import ModelForm
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CadastroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'nome', 'email', 'numero', 'status', 'foto')


class atualizarCadastroForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('username', 'nome', 'email', 'numero', 'status', 'foto')


class LoginForm(ModelForm):
    class Meta:
        model = Usuario
        fields = []
