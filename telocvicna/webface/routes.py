from . import app
from flask import render_template, request, flash,url_for,redirect
from pony.orm import db_session, select
from .models import Uzivatel
from werkzeug.security import check_password_hash
@app.route('/')
def index():
    """
    login = request.form.get("login")
    heslo = request.form.get("heslo")
    print(login)
    with db_session:
        uzivatel = Uzivatel.get(login=login)
        if uzivatel:
            pwhash = uzivatel.heslo
        else:
            pwhash = None
    check_password_hash(pwhash,heslo)
    """
    return render_template('base.html.j2')

@app.route("/login/")
def login():
    return render_template("login.html.j2")

@app.route("/login/",methods=["POST"])
def login_post():
    username = request.form.get("login")
    password = request.form.get("password")
    if username and password:
        with db_session:
            uzivatel = Uzivatel.get(login=username)
            if uzivatel:
                zadane_heslo = password
                heslo = uzivatel.heslo
                if zadane_heslo == heslo:
                    flash("Úspěšné přihlášení")
    return redirect(url_for("tajna"))
@app.route("/tajna/")
def tajna():
    return render_template("tajna.html.j2")
