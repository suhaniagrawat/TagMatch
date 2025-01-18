import sqlite3
from fastapi import FastAPI, HTTPException
from typing import List, Dict

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to the TagMatch API server. Kindly visit http://127.0.0.1:8000/docs to see the search results for products."}

# Table mappings for mobile and laptop categories
TABLES = {
    "mobile": [
        "mobilephones_data_site1",
        "mobilephones_data_site2"
    ],
    "laptop": [
        "laptops_data_site1",
        "laptops_data_site2"
    ]
}

# Helper function to fetch data from the SQLite database with partial matching
def fetch_data_from_table(conn, table_name, product_name):
    # Use the LIKE operator for partial matching (case-insensitive)
    query = f"SELECT Name_name, Name_url, Name_Price FROM {table_name} WHERE Name_name LIKE ?"
    cursor = conn.execute(query, ('%' + product_name + '%',))  # Wildcard for partial matching
    return cursor.fetchall()

# Endpoint to fetch product data
@app.get("/fetch-product/")
async def fetch_product(product_name: str, category: str):
    if category not in TABLES:
        raise HTTPException(status_code=400, detail="Invalid category. Use 'mobile' or 'laptop'.")

    db_path = "database.db"
    results = {}

    try:
        conn = sqlite3.connect(db_path)
        # Fetch data from both sites based on the category
        for site_index, table_name in enumerate(TABLES[category]):
            data = fetch_data_from_table(conn, table_name, product_name)
            if data:
                site_key = f"site{site_index + 1}"
                results[site_key] = []
                for row in data:
                    results[site_key].append({
                        "product_name": row[0],
                        "Name_url": row[1],
                        "Name_Price": row[2],
                    })
        conn.close()
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

    if not results:
        raise HTTPException(status_code=404, detail="No products found.")

    return {
        "product_name": product_name,
        "category": category,
        "results": results
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
