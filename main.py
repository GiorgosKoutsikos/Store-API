from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Store!"}

class Product(BaseModel):
    name: str
    price: float
    description: str = ""
    stock: int = 0


products = []
@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return {"message": "Product created successfully", "product": product}

@app.get("/products")
def get_products():
    return products
