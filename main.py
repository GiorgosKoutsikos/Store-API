from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Store!"}

class Product(BaseModel):
    id: int | None = None
    name: str
    price: float
    description: str = ""
    stock: int = 0


products = []
@app.post("/products")
def create_product(product: Product):
    product.id = len(products) + 1
    products.append(product)
    return {"message": "Product created successfully", "product": product}

@app.get("/products")
def get_products():
    return products

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product_id == product.id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
