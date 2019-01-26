from bs4 import BeautifulSoup
from urllib import urlopen

BASE_URL = "http://garfieldminusgarfield.net/archive/"

def format_url(year, month):
    return BASE_URL + str(year) + "/" + str(month)

def format_post_id(year, month):
    tens_place = ""
    if month <= 9:
        tens_place = "0"
    return "posts_" + str(year) + tens_place + str(month)

posts_year = 2018
posts_month = 3

html = urlopen(format_url(posts_year, posts_month))
soup = BeautifulSoup(html, 'html.parser')
print("id = " + format_post_id(posts_year, posts_month))
post_id = format_post_id(posts_year, posts_month)
current_month_div = soup.find(id=post_id)

for 