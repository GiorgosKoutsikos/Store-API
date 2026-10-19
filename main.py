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

class ProductUpdate(BaseModel):
    name: str
    price: float
    description: str = ""
    stock: int = 0

@app.put("/product/{product_id}")
def update_product(product_id: int, updated_product: ProductUpdate):
    for product in products:
        if product_id == product.id:
          product.name = updated_product.name
          product.price = updated_product.price
          product.description = updated_product.description
          product.stock = updated_product.stock
          return{"message": "Product updated successfully", "product": product}
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product_id == product.id:
            products.remove(product)
            return{"message": "Product successfully deleted", "product": product}
    raise HTTPException(status_code=404, detail="Product not found")
