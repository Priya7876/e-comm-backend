import jwt
from datetime import datetime,timedelta
from app.config import SECRET_KEY

def create_access_token(username):
    payload ={
        "username" : username,
        "exp" : datetime.utcnow() + timedelta(hours=1)

    }
    return jwt.encode(payload,SECRET_KEY,algorithm="HS256")

def verify_token(token):
    try:
        decoded= jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
        return decoded["username"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvaildTokenError:
        return None