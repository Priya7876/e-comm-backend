from app.models.user import User
from flask import json , request,jsonify
from app.utils.jwt  import create_access_token

def register_user_routes(app):
    @app.route("/users/register" , methods=["POST"])
    def register():
        data= request.json
        username= data["username"]
        password= data["password"]
        user =User.find_by_username(username)
        if(user):
            return jsonify({"Error" : "Username already exists"}),400
        User.create_user(username,password)
        return jsonify({"message" : "The user is added successfully "}),200
    
    @app.route("/users/login" ,methods=["POST"])
    def login():
        data = request.json
        username = data["username"]
        password = data["password"]
        user = User.find_by_username(username)
        if(not user and not User.verify_password(password,user["password"])):
            return jsonify({"error" :"Something went wrong"}),400
        token= create_access_token(username)
        return jsonify({"access_token": token}),200
        


        
