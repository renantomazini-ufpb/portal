from flask import Flask, render_template, session, request, redirect, url_for




app = Flask(__name__)

app.secret_key = '123456'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/error")
def error():
    return render_template("error.html")



@app.route("/dash")
def dash():
    if 'username' in session:
        return render_template("dash.html", username=session['username'])
    return "<h1>acesso negado</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '123456':
            session['username'] = username
            return redirect(url_for('dash'))
        else:
            return render_template("error.html", message="Seu login falhou, verifique a senha ou login")
    
    return redirect(url_for('error'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

