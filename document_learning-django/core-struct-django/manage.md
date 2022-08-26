# **Anotacões de Padrão de projeto Django**
### django 2.1.5 | Python 3.7

## manage
 - É um wrapper em volta do django-admin
 - Ele delega tarefas para o django-admin
 - Responsável por colocar o pacote do projeto no sys.path
 - ele define a variável de ambiente DJANGO_SETTINGS_MODULE que então aponta
para o arquivo settings.py
 - Por isso, o manage.py é gerado automaticamente junto ao projeto, para
facilitar o uso de comandos do django-admin.py (comandos administrativos)
