# Comandos 
 mkdir 02-database-manager --- Criar um Diretorio
 cd .\.flask-masterclass\

 python -m venv .venv
 pip install flask-bootstrap
 pip install SQLAlchemy
 
 # Criar ambiente vitual
 -- .venv => Nome do ambiente
.flask-masterclass> python -m venv .venv

#### Ativando um projeto
 .\.venv\Scripts\Activate.ps1
 
#### Desativa ambiente
(.venv) ... pasta ... deactivate

# Execultar a aplicação
 python .\app.py

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

## Criar banco de dados
>>> app
<Flask 'app'>
>>> from app import db
>>> db.create_all()

##Instalar o flask_login
pip install flask-login==0.4.1   

## criando o venv e intalando todas as bibiotecas
python -m venv .refactory
.\.refactory\Scripts\Activate.ps1
pip install -r .\requirements.txt

