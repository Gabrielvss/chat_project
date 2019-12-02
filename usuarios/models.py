from django.db import models
from django.contrib.auth.models import AbstractUser


class Pais(models.Model):
    '''nao serve pra nada'''
    nome = models.CharField(max_length=40)

    def __str__(self):
        return self.nome


class Usuario(AbstractUser):
    '''Classe padrão de usuarios'''
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, default='')
    numero = models.CharField(max_length=15)
    status = models.CharField(max_length=100)
    foto = models.ImageField(
        upload_to='images/', blank=True, default='images/Screenshot_2.png')

    def __str__(self):
        return self.username


class Chat(models.Model):
    '''Classe que gera as mensagens'''
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        Usuario, on_delete=models.DO_NOTHING, related_name='QuemEnviou')
    remetente = models.ManyToManyField(Usuario)
    mensagem = models.TextField()

    def __str__(self):
        return self.mensagem

    def __repr__(self):
        return self.mensagem

    @classmethod
    def create_msg(cls, current_user, remetente1, msg):
        '''cria uma nova mensagem'''
        chat, created = cls.objects.get_or_create(
            user=current_user, mensagem=msg
        )
        chat.remetente.set(remetente1)
        return chat


class Friend(models.Model):
    '''classe amigo'''
    users = models.ManyToManyField(Usuario)
    current_user = models.ForeignKey(
        Usuario, related_name='owner', null=True, on_delete=models.DO_NOTHING)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        '''adiciona amigos a lista'''
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        '''remove amigos da lista'''
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)
