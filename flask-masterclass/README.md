# Comandos 
 cd .\.flask-masterclass\
 
# Criar ambiente vitual
.flask-masterclass> python -m venv .venv

#### Ativando um projeto
 .\.venv\Scripts\Activate.ps1
 
#### Desativa ambiente
(.venv) ... pasta ... deactivate

#### Remover o ambiente
 rm -r .venv
 

### Novo ambiente
  python -m venv .flask-masterclass
  
 .\Scripts\Activate.ps1   

### Intalando o flask
pip install flask

### Atualizando o pip
python -m pip install --upgrade pip

### Criar variavel de ambiente no powerShell
set FLASK_APP=app 

















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

