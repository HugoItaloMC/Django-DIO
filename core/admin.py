from django.contrib import admin
#  from core.models import 'AquiVoceImporta_ATabelaAplicada_ComoUmaClasse'
# Register your models here.
"""

 # Para iniciar vc cria o mesmo nome da tabela importada com 'Admmin' na frente, 
no exemplo abaixo ultilizamos a palavra 'Pessoa' como exemplo  
 
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nome')
    list_filter = ('nome',)

admin.site.register(TabelaImportada)

OBS :  No arquivo urls.py como default já com setando o caminho da interface administrativa 
urlpatterns = [
    path('admin/', admin.site.urls),  # Aqui está setado o caminho da interface administrativa;
    path('soma/<int:n1>/<int:n2>', views.soma),
    path('sub/<int:n1>/<int:n2>', views.sub),
    path('divi/<int:n1>/<int:n2>', views.divi)
]

"""