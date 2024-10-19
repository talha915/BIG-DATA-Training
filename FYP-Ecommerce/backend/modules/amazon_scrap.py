from bs4 import BeautifulSoup
import requests
import pandas as pd


URL = "https://www.amazon.com/s?k=samsung+galaxy+s24"


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5",
}


webpage = requests.get(URL, headers=HEADERS)


if webpage.status_code == 200:
    soup = BeautifulSoup(webpage.content, "html.parser")

    titles = soup.find_all("span", class_="a-size-medium a-color-base a-text-normal")

    prices = soup.find_all("span", class_="a-offscreen")

    images = soup.find_all("img", class_="s-image")

    products = []

    for title, price, image in zip(titles, prices, images):
        products.append(
            {
                "Title": title.get_text(),
                "Price": price.get_text(),
                "Image URL": image["src"],
            }
        )

    df = pd.DataFrame(products)
    print(df)
else:
    print("Failed to retrieve the webpage. Status code:", webpage.status_code)
