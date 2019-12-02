
Desenvolvimento de uma aplicação com chat para conversas em tempo real ultilizando o
Django.

Nesta pasta, crie e ative um ambiente virutal com os seguintes comandos no terminal:


No Windows:

virtualenv env
cd env/Scripts
activate


Instale as bibliotecas necessarias:

pip install django
pip install django-bootstrap-form
pip install Pillow


Em seguida, utilize os codigos:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Acesse o site pelo ip/porta/login/


O sistema possui um usuario padrão previamente cadastrado:
usuario : usuariopadrao
senha: usuariopadrao123
