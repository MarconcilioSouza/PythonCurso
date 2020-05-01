# Comandos 
PS C:\Users\*\source\repos\PythonCurso\flask-masterclass> cd .\.flask-masterclass\
PS C:\Users\*\source\repos\PythonCurso\flask-masterclass\.flask-masterclass> .\Scripts\Activate.ps1   

# Execultar a aplicação
 (.flask-masterclass) PS C:\Users\meunote\source\repos\PythonCurso\flask-masterclass\introducao> python .\app.py

#### Ativando um projeto
PS C:\Users\meunote\source\repos\PythonCurso\flask-masterclass\02-database-manager> .\.venv\Scripts\Activate.ps1

 mkdir 02-database-manager --- Criar um Diretorio
 python -m venv .venv
 pip install flask-bootstrap
 pip install SQLAlchemy

## Set a variavel de ambiente do flask
(.venv) PS C:\Users\meunote\source\repos\PythonCurso\flask-masterclass\02-database-manager> set FLASK_APP=app
(.venv) PS C:\Users\meunote\source\repos\PythonCurso\flask-masterclass\02-database-manager> flask
### Entra no shell do flask
(.venv) PS C:\Users\NoteCasa\source\repos\PythonCurso\flask-masterclass\02-database-manager> flask shell
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
App: app [production]
Instance: C:\Users\NoteCasa\source\repos\PythonCurso\flask-masterclass\02-database-manager\instance
>>> app
<Flask 'app'>
>>> from app import db
>>> db.create_all()
>>>

