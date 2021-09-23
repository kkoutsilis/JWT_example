from re import I
from app.api import api_bp
from flask import jsonify
from app.utils import authenticate_restful


@api_bp.route("/route1", methods=["GET"])
def route1():
    return jsonify(message="This route is accessible by anyone")


@api_bp.route("/route2", methods=["GET"])
@authenticate_restful
def route2(resp):
    return jsonify(message="This route is accessible by authetciated users")
