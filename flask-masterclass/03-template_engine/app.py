from flask import Flask, render_template, flash
from datetime import datetime
from filtros import format_date


app = Flask(__name__, 
template_folder="tema", 
static_folder="public")
app.config["SECRET_KEY"] = "secret"
app.jinja_env.filters["format_date"] = format_date

@app.route("/templates")
def template():
    user_page = True
    return render_template("index.html", user_page=user_page)


@app.route("/Usuarios")
def users():
    users = [{
        "name": "Marconcilio Souza",
        "age": 35,
        "email": "marco@hotmail.com",
        "active": True,
        "since": datetime.utcnow()
    },
    {
        "name": "amanda souza",
        "idade": 28,
        "email": "oi@hotmail.com",
        "active": False,
        "since": datetime.utcnow()
    }]
    flash(message="User routes", category="success")
    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)