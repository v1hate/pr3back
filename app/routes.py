from flask import Blueprint, request, jsonify
from .models import db, User

main = Blueprint('main', __name__)

@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # Aquí la lógica para registrar al usuario
    new_user = User(username=username, password=password)  # Asegúrate de hashear la contraseña
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Usuario registrado exitosamente"}), 201

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    # Aquí la lógica para autenticar al usuario
    user = User.query.filter_by(username=username).first()
    if user and user.password == password:  # Asegúrate de verificar la contraseña correctamente
        return jsonify({"token": "token_de_autenticación"}), 200
    return jsonify({"message": "Credenciales incorrectas"}), 401

@main.route('/send-message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data.get('message')
    # Aquí la lógica para guardar el mensaje en la base de datos
    return jsonify({"message": "Mensaje enviado"}), 200
