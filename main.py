from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, Product
from schemas import ProductCreate

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Price Comparison API"}

# Fetch all products
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

# Add a new product
@app.post("/add-product")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    new_product = Product(
        name=product.name,
        store=product.store,
        price=product.price,
        url=product.url,
        rating=product.rating
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
