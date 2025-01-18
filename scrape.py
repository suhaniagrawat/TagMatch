from bs4 import BeautifulSoup

# Path to the HTML file
html_file_path = "/Users/guddu/Desktop/Envisage/html.txt"  # Replace with the actual path

# Load and parse the HTML file
with open(html_file_path, "r", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# Extract mobile names and prices based on class names
mobile_names = soup.find_all("div", class_="offer-products__detailsName")
mobile_prices = soup.find_all("div", class_="product_offer__priceNew")

print(soup.prettify())

# Print the extracted details
for name, price in zip(mobile_names, mobile_prices):
    print(f"Mobile: {name.text.strip()}, Price: {price.text.strip()}")
