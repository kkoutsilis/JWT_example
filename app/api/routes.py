from re import I
from app.api import api_bp
from flask import jsonify
from app.utils import authenticate_restful, authorized


@api_bp.route("/public", methods=["GET"])
def public():
    return jsonify(message="This route is accessible by anyone")


@api_bp.route("/authenticated", methods=["GET"])
@authenticate_restful
def authenticated(resp):
    return jsonify(message="This route is accessible by authetciated users")


@api_bp.route("/authorized", methods=["GET"])
@authorized
def authorized(resp):
    return jsonify(message="This route is accessible by admin users")
