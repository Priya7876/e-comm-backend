
from flask import json , request,jsonify
from app.extensions import mongo
from app.models.products import Product

def products_routes(app):
    @app.route("/add_products" , methods=["POST"])
    def add_product():
        data = request.json
        product = Product.from_dict(data)
        mongo.db.products.insert_one(product.to_dict())
        return jsonify({"messsage:" : "Product is successfully added to the list"}), 201
    
    @app.route("/products" , methods = ["GET"])
    def get_products():
        products = list(mongo.db.products.find())
        for product in products:
            product["_id"]=str(product["_id"])

        return jsonify(products),201
    @app.route("/products/<product_id>" , methods=["GET"])
    def get_product(product_id):
        product = mongo.db.products.find_one({"_id": mongo.ObjectId(product_id)})
        if not product:
            return jsonify({"message" : "Product doesnt exist"}),400
        return jsonify(product),201

    


    


        
