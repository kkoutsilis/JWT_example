from functools import wraps
from flask import request, jsonify
from app.models import User


def authenticate(f):
    @wraps(f)
    def decorated_fucntion(*args, **kwargs):
        response_object = {"status": "fail", "message": "Provide a valid auth token."}
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return jsonify(response_object), 403
        auth_token = auth_header.split(" ")[1]
        sub, adm = User.decode_auth_token(auth_token)
        if isinstance(sub, str):
            response_object["message"] = sub
            return jsonify(response_object), 401
        user = User.query.filter_by(id=sub).first()
        if not user or not user.active:
            return jsonify(response_object), 401
        return f(sub, *args, **kwargs)

    return decorated_fucntion


def authenticate_restful(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response_object = {"status": "fail", "message": "Provide a valid auth token."}
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return response_object, 403
        auth_token = auth_header.split(" ")[1]
        sub, adm = User.decode_auth_token(auth_token)
        if isinstance(sub, str):
            response_object["message"] = sub
            return response_object, 401
        user = User.query.filter_by(id=sub).first()
        if not user or not user.active:
            return response_object, 401
        return f(sub, *args, **kwargs)

    return decorated_function


def authorized(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response_object = {
            "status": "fail",
            "message": "Admin rights requred to access this resource.",
        }
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return response_object, 403
        auth_token = auth_header.split(" ")[1]
        sub, adm = User.decode_auth_token(auth_token)
        if isinstance(sub, str):
            response_object["message"] = sub
            return response_object, 401
        user = User.query.filter_by(id=sub).first()
        if not user or not user.active:
            return response_object, 401
        if adm != True:
            return response_object, 403
        return f(sub, *args, **kwargs)

    return decorated_function


def is_admin(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user.admin
