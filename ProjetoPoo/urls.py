"""ProjetoPoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from usuarios.views import messagesT, Post, talk_to, cadastro, listagem, update, delete, login_view, submit_login, index, logout, change_friends

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastro/', cadastro, name='url_cadastro'),
    path('atualizar/<int:pk>', update, name='url_atualizar'),
    path('delete/<int:pk>', delete, name='url_delete'),
    path('', listagem, name='url_listagem'),
    path('login/', login_view, name='url_login'),
    path('login/submit', submit_login, name='url_submit_login'),
    path('login/index/', index, name='url_index'),
    path('logout/', logout, name='url_logout'),
    path('connect/<operation>/<pk>/', change_friends, name='change_friends'),
    path('login/index/chat/<pk>/', talk_to, name='talk_to'),
    path('post/<pk>/', Post, name='post'),
    path('messages/<pk>/', messagesT, name='messages')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
