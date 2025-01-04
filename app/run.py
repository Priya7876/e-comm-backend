from flask import Flask;
from app.extensions import mongo
from app.routes.authen_routes import register_user_routes
from app.routes.products_routes import products_routes
def create_app():
    app=Flask(__name__)
    app.config.from_pyfile("config.py")
    mongo.init_app(app)
    register_user_routes(app)
    products_routes(app)
    return app