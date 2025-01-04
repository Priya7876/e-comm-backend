from app.extensions import mongo

class Product :
    def __init__(self, name , description , price , stock):
        self.name = name
        self.description = description
        self.price= price
        self.stock = stock

    def to_dict(self):
        return {
            "name": self.name,
            "description" :self.description,
            "price" : self.price,
            "stock" : self.stock
        }
    @staticmethod
    def from_dict(data) :
        return Product(
            name = data["name"],
            description=data["description"],
            price= data["price"],
            stock = data["stock"]
        )
    
        
