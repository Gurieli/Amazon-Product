import requests
from bs4 import BeautifulSoup
import smtplib

AMAZON_URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"


headers = {
    "Accept-Language":"en-US,en;q=0.9,ka;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
                 " (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}
response = requests.get(url=AMAZON_URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(name="span", class_="a-offscreen").getText()
price = float(price.split("$")[1])

if price < 10:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)




