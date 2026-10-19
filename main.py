from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
from database import engine, get_db

#Auto-create tables in database
models.Base.metadata.create_all(bind=engine)

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



@app.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):
    db_product = models.ProductModel(
        name = product.name,
        price = product.price,
        description = product.description,
        stock = product.stock
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return {"message": "Product created successfully", "product": db_product}

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    all_products = db.query(models.ProductModel).all()
    return all_products

@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.ProductModel).filter(models.ProductModel.id == product_id).first()

    if not product:
      raise HTTPException(status_code=404, detail="Product not found")

    return product

class ProductUpdate(BaseModel):
    name: str
    price: float
    description: str = ""
    stock: int = 0

@app.put("/product/{product_id}")
def update_product(product_id: int, updated_product: ProductUpdate, db: Session = Depends(get_db)):
    product = db.query(models.ProductModel).filter(models.ProductModel.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.name = updated_product.name
    product.price = updated_product.price
    product.description = updated_product.description
    product.stock = updated_product.stock

    db.commit()
    db.refresh(product)

    return{"message": "Product updated successfully", "product": product}



@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.ProductModel).filter(models.ProductModel.id == product_id).first()

    if not product:
         raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return{"message": "Product successfully deleted", "product": product}
