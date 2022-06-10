# ................. Amazon Price Tracker project ........................ #
# ......... Created and modified by N.S.bhanuprakash on 30-04-2022 ...... #
import os
import requests
from bs4 import BeautifulSoup
from smtplib import SMTP
from twilio.rest import Client

product_URL = "https://www.amazon.in/Seagate-Expansion-1TB-External-HDD/dp/B08ZJDWTJ1/?" \
              "_encoding=UTF8&pd_rd_w=2GO94&pf_rd_p=ee853eb9-cee5-4961-910b-2f169311a086&" \
              "pf_rd_r=T3HXCASTB11286BBSJ6Q&pd_rd_r=0278be96-8ac9-46f8-a7bf-31de66181cb6&pd_rd_wg=UbYTG&" \
              "ref_=pd_gw_ci_mcx_mr_hp_atf_m"
# "https://www.amazon.com/dp/B0053WRWX8/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
headers = {
    "Accept-Language": "en,en-US;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/100.0.4896.127 Safari/537.36"
}
TARGET_PRICE = 4000
CURRENCY = "₹"
# "$"

response = requests.get(url=product_URL, headers=headers)
with open("website.html", "w", encoding="utf-8",) as file:
    file.write(response.text)
print(response.status_code)

with open("website.html",  encoding="utf-8") as file:
    website_html = file.read()
soup = BeautifulSoup(website_html, "html.parser")
product_price_line = soup.find(name="span", class_="a-offscreen")
product_price = float(product_price_line.string.split(CURRENCY)[1].replace(",", ""))
product_name = soup.find(name="span", id="productTitle").get_text().strip()
# print(product_price, product_name, product_URL)

# .................. If you want to mail a person ........................................... #
# from_address = "smtptrial22@gmail.com"
# mail_password = os.getenv("mail_password")
# to_address = "nsbprakash95@gmail.com"
# smtp_server = "smtp.gmail.com"
#
# email_msg = f"Subject:Low price alert for {product_name}\n\n" \
#             f"'{product_name}' is available for {CURRENCY}{product_price}." \
#       f" Hurry Up! Go and buy at {product_URL}".encode("utf-8")
# if product_price <= TARGET_PRICE:
#     with SMTP(host=smtp_server, port=587) as smtp_obj:
#         smtp_obj.starttls()
#         smtp_obj.login(user=from_address, password=mail_password)
#         smtp_obj.sendmail(from_addr=from_address, to_addrs=to_address, msg=email_msg)
# ........................................................................................... #

# .................. If you want to message a person ........................................... #
twilio_sid = os.getenv("twilio_sid")
twilio_auth_token = os.getenv("twilio_auth_token")
client = Client(twilio_sid, twilio_auth_token)
sms_msg = f"Low price alert! '{product_name}' is available for {CURRENCY}{product_price}." \
      f" Hurry Up! Go and buy at {product_URL}"
to_numbers = ['+91xxxxxxxxxx', '+91xxxxxxxxxx']

if product_price <= TARGET_PRICE:
    for number in to_numbers:
        message = client.messages.create(
            body=sms_msg,
            from_=os.getenv("my_twilio_num"),
            to=number,
        )
        print(message.status)
# ........................................................................................... #
