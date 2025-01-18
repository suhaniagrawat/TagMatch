# models.py

from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

# Create the base class for our models
Base = declarative_base()

# Define the Product model class
class Product(Base):
    __tablename__ = "products"  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)  # Primary key for the product
    name = Column(String, index=True)  # Product name
    store = Column(String)  # Store name
    price = Column(Float)  # Product price
    url = Column(String)  # URL of the product
    rating = Column(Float)  # Product rating
    

# Create an SQLite database and engine
engine = create_engine("sqlite:///database.db")  # SQLite database file

# Create session maker to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the tables in the database (it will create `products` table)
Base.metadata.create_all(bind=engine)
