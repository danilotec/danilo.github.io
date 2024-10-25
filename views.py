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

last_reader = None

@app.route('/data', methods=['POST'])
def receive_data():
    global last_reader  
    data = request.get_json()

    if 'leitura' in data:
        last_reader = data['leitura'] 
        print(f'receive: {last_reader}')
        return jsonify(
            {
                "status": "success",
                "reader": last_reader 
            }
        ), 200
    else:
        return jsonify(
            {
                "status": "error",
                "message": "data not found"
            }
        ), 400

@app.route('/display')
def display_data():
    return render_template('display.html', leitura=last_reader) 