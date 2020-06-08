from flask import Flask, render_template, flash

app = Flask(__name__, template_folder="tema")
app.config["SECRET_KEY"] = "secret"


@app.route("/templates")
def template():
    users = {
        "name": "Marconcilio Souza",
        "idade": 35,
        "email": "marco@hotmail.com"
    }

    flash("usuário criado com sucesso!")
    return render_template("index.html", users=users)


@app.route("/users")
def users():
    flash("usuário criado com sucesso!")

    return render_template("users.html")


if __name__ == "__main__":
    app.run(debug=True)