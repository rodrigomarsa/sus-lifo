from flask import Blueprint, jsonify, request

user_controller = Blueprint("user_controller", __name__)


@user_controller.route("/users", methods=["GET"])
def all_users():
    from models.user_model import Users

    users = Users.get_all_users()
    if users:
        return jsonify([user.to_dict() for user in users]), 200
    return jsonify({"message": "Nenhum paciente cadastrado"}), 404


@user_controller.route("/new", methods=["POST"])
def new_user():
    from models.user_model import Users

    name = request.json["name"]
    if not name:
        return jsonify({"message": "Nome não pode ser vazio"}), 400
    Users.add_user(name)
    return jsonify({"message": "Paciente cadastrado com sucesso"}), 201
