from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import mongo
class User:
    @staticmethod
    def find_by_username(username):
        return mongo.db.users.find_one({"username" : username})
    
    @staticmethod
    def create_user(username, password):
        hashed_password = generate_password_hash(password)
        return mongo.db.users.insert_one({"username" : username , "password" : hashed_password})
    
    @staticmethod
    def verify_password(stored_passwd, provided_passwd):
        return check_password_hash(stored_passwd,provided_passwd)