from flask import Flask, render_template, flash

app = Flask(__name__, 
template_folder="tema", 
static_folder="public")
app.config["SECRET_KEY"] = "secret"


@app.route("/templates")
def template():
    user_page = True
    return render_template("index.html", user_page=user_page)


@app.route("/Usuarios")
def users():
    users = [{
        "name": "Marconcilio Souza",
        "idade": 35,
        "email": "marco@hotmail.com",
        "active": True
    },
    {
        "name": "Amanda Souza",
        "idade": 28,
        "email": "oi@hotmail.com",
        "active": False
    }]
    flash("usuário criado com sucesso!")
    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)