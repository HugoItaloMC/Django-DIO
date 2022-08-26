# **Anotacões de Padrão de projeto Django**
### django 2.1.5 | Python 3.7

##  wsgi
 - Web Server Gateway Interface - Interface de porta de entrada 
do servidor web. Uma plataforma padrão para aplicacões web
 - Serve de interface do Servidor Web e a Aplicacão Web. O Django
com o comando startproject inicia uma configuracão WSGI padrão para que
se possa executar sua aplicacão qwb.
 - Quando se inicia a aplicacão em Django com o comando runserver é iniciado um
servidor de aplicacão web leve. Esse servidor é especificado pela configuracão
WSGI_APPLICATION
obs: Toda Aplicacão web necessita de um servidor de aplicacão, um exemplo 
conhecido é o apache, sem essa interface somente servidores com suporte a linguagem
podem hospedar a aplicacão. E que esse tipo de servidor é um ambiente de desenvolvimento
para hospedar para uma aplicacão para um cliente ultilize um servidor mais robusto