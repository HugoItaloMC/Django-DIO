# **Anotacões de Padrão de projeto Django**
### django 2.1.5 | Python 3.7

## models
 - Define o modelo de dados inteiramente em Python. Faz a abstracão dos objetos para o Python,
transformando todas as tabelas em classes e os acessos são feitos ultilizando a linguagem
Python com uma estrutura em Classes, onde o Django realiza a conversão para SQL
exemplos de como fazer uma requisicão em uma tabela. 
 python: pessoa = Pessoa.objects.get(nome="Safe") 
 SQL: select * from pessoa where nome = "Safe";
 OBS: Não importa em qual banco de dados a aplicacão esteja conectada, oracle, MySQL, PostgreSQL
o Django reconhece o SGBD e aplica o padrão de SQL referente .