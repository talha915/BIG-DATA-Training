from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL jise scrape karna hai
URL = "https://www.amazon.com/s?k=samsung+galaxy+s24"

# HTTP headers set karen
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}

# Webpage ko request karen
webpage = requests.get(URL, headers=HEADERS)

# Response ka status check karein
if webpage.status_code == 200:
    # Page ka content parse karein
    soup = BeautifulSoup(webpage.content, "html.parser")

    # Product titles ko find karein
    titles = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")

    # Prices ko find karein
    prices = soup.find_all("span", class_="a-offscreen")

    # Images URLs ko find karein
    images = soup.find_all("img", class_="s-image")

    # Data store karne ke liye list banayen
    products = []

    # Titles, Prices, aur Images URLs ko combine karein
    for title, price, image in zip(titles, prices, images):
        products.append(
            {
                "Title": title.get_text(),
                "Price": price.get_text(),
                "Image URL": image["src"],  # Image ka URL
            }
        )

    # DataFrame banayen aur print karein
    df = pd.DataFrame(products)
    print(df)
else:
    print("Failed to retrieve the webpage. Status code:", webpage.status_code)
