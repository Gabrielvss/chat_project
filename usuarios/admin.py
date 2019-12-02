from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .forms import CadastroForm, atualizarCadastroForm
from .models import Usuario, Friend


class Administador(UserAdmin):
    add_form = CadastroForm
    form = atualizarCadastroForm
    model = Usuario
    list_display = ['email', 'username']


admin.site.register(Usuario, Administador)

admin.site.register(Friend)
