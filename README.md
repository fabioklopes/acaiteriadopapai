# Configuração do Projeto
Use estes comandos para criar um ambiente virtual dentro da pasta do seu projeto, ativar o ambiente virtual e em seguida importar as respectivas dependências. A execução dos comandos devem seguir a seguinte ordem: 
```
py -m venv venv
```
Se você usa Windows, use este comando para ativar o ambiente virtual:
```
.\venv\Scripts\activate
```
Se você usa Linux, use este: 
```
source venv/bin/activate
```
Em seguida, faça a importação das dependências:
```
pip install -r requirements.txt
```

# Execução do Projeto
Execute este comando para iniciar o servidor embutido no ambiente virtual:
```
py manage.py runserver
```
Você verá algo desse tipo:
> **Watching for file changes with StatReloader**
> Performing system checks...
> 
> System check identified no issues (0 silenced).
> July 27, 2025 - 17:23:55
> Django version 5.2.4, using settings 'core.settings'
> Starting development server at _http://127.0.0.1:8000/_
> Quit the server with CTRL-BREAK.
> 
> WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.
> For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/
