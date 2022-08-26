#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    #  Setando a Variável de ambiente DJANGO_SETTINGS_MODULE para o projeto project_learning.settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_learning.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    #  Colocando o pacote dentro do PATH do sys:
    execute_from_command_line(sys.argv)

"""
 Finalizando o processo do módulo ele termina de delegar os processos para django-admin.md,
sem essa camada de execucão teriámos que fazer isso manualmente para indicar aonde se encontra 
as configuracões padrões do framework.
"""
