import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2,40):  
    url = "https://www.flipkart.com/search?q=moblile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    boxes = soup.find_all("div", class_="DOjaWF gdgoEp")

    for box in boxes:
        name = box.find("div", class_="KzDlHZ")
        price = box.find("div", class_="Nx9bqj _4b5DiR")
        desc = box.find("ul", class_="G4BRas")
        review = box.find("div", class_="XQDdHH")  # Some products may not have reviews

        # Append data, ensuring all lists have the same length
        Product_name.append(name.text if name else "N/A")
        Prices.append(price.text if price else "N/A")
        Description.append(desc.text if desc else "N/A")
        Reviews.append(review.text if review else "N/A")  # Handle missing reviews

# Print lengths to verify they are the same
print(len(Product_name), len(Prices), len(Description), len(Reviews))

# Create DataFrame
df = pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Description": Description, "Reviews": Reviews})
#print(df)
df.to_csv("flipkart_mobile_under_50k.csv")