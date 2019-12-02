from django.shortcuts import render, redirect
from .models import Usuario, Friend, Chat
from .forms import CadastroForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


def Post(request, pk):
    '''posta mensagens'''
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, mensagem=msg)
        msg = c.user.username+": "+msg
        c = Chat(user=request.user, mensagem=msg)
        if msg != '':
            c.save()
        return JsonResponse({'msg': msg, 'user': c.user.username})
    else:
        return HttpResponse('Request must be POST.')


@login_required(login_url='/login/')
def index(request):
    '''carrega a pagina de entrada, depois do login'''
    usuario = {}
    try:
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
    except Friend.DoesNotExist:
        friends = {}
    usuario['amigos'] = friends
    usuario['self'] = request.user
    usuario['usuarios'] = Usuario.objects.all()
    usuario['AmigoChat'] = {}
    return render(request, 'index.html', usuario)


def logout(request):
    '''realiza o logout'''
    django_logout(request)
    return redirect('/login/')


def cadastro(request):
    '''carrega a pagina de cadastro'''
    context = {}
    form = CadastroForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect('/login/')

    context['form'] = form
    return render(request, 'cadastro.html', context)


def login_view(request):
    '''carrega a pagina de login'''
    return render(request, 'login.html')


@csrf_protect
def submit_login(request):
    '''realiza o submit do form de login'''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index/')
        else:
            messages.error(
                request, 'Usuário ou senha invalidos, tente novamente')
    return redirect('/login/')


def listagem(request):
    '''carrega a pagina de listagem'''
    data = {}
    data['usuarios'] = Usuario.objects.all()

    return render(request, 'listagem.html', data)


def update(request, pk):
    '''carrega a pagina de atualização dos dados do usuario'''
    data = {}
    usuario = Usuario.objects.get(pk=pk)
    form = CadastroForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('url_index')

    data['form'] = form
    return render(request, 'cadastro.html', data)


def delete(request, pk):
    '''deleta um usuario do banco'''
    usuario = Usuario.objects.get(pk=pk)
    usuario.delete()
    return redirect('url_listagem')


def change_friends(request, operation, pk):
    '''remove ou adiciona amigos'''
    new_friend = Usuario.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.remove_friend(request.user, new_friend)
    return redirect('/login/index/')


@login_required(login_url='/login/')
def talk_to(request, pk):
    '''carrega a pagina para entrar em contato com cada a amigo da lista de amigos'''
    usuario = {}
    try:
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
    except Friend.DoesNotExist:
        friends = {}
    usuario['amigos'] = friends
    usuario['self'] = request.user
    usuario['usuarios'] = Usuario.objects.all()
    usuario['AmigoChat'] = Usuario.objects.get(pk=pk)
    return render(request, 'index.html', usuario)


def messagesT(request, pk):
    '''carrega as mensagens constantemente buscando por novas'''
    rementente = Usuario.objects.get(pk=pk)
    chat = {}
    c = Chat.objects.all()
    chat['chat'] = c
    return render(request, 'messages.html', chat)
