from flask import render_template, request, redirect, url_for, jsonify

from app import app
from api import enviar_mensagem

db = []
banco = ''

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/receber', methods=['POST'])
def receber():
    email = request.form['email_input']
    mensagem = request.form['message_input']
    
    if email and mensagem:
        db.append(
            f'email: {email}\nmensagem: {mensagem}'
            )
        global banco #pessima maneira de usar uma variavel, porem como teste funciona
        banco = db[-1]
        enviar_mensagem(db[-1])

        if len(db) > 3:
            db.clear()
            
    return redirect(url_for('index'))

@app.route('/admin')
def admin():
    return render_template('admin.html', banco_dados=banco)

@app.route('/clear', methods=['POST'])
def clear():
    db.clear()
    return redirect(url_for('admin'))

