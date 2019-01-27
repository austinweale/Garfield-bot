from bs4 import BeautifulSoup
from urllib import urlopen

#This script grabs all of the garfield minus garfield images month by month from the tumblr archive

BASE_URL = "http://garfieldminusgarfield.net/archive/"

#Take the current year and month and return a url for that month's comics
def format_url(year, month):
    return BASE_URL + str(year) + "/" + str(month)

#Take current year and month and return the post-id for the div with that month's comics
def format_post_id(year, month):
    tens_place = ""
    if month <= 9:
        tens_place = "0"
    return "posts_" + str(year) + tens_place + str(month)

posts_year = 2017
posts_month = 9

#Get full page html
html = urlopen(format_url(posts_year, posts_month))
html_page = BeautifulSoup(html, 'html.parser')

#get html for current month's comics
print("id = " + format_post_id(posts_year, posts_month))
post_id = format_post_id(posts_year, posts_month)
current_month_div = html_page.find(id=post_id)
div_doc = BeautifulSoup(str(current_month_div), 'html.parser')
print(div_doc.prettify())

links = div_doc.find_all("a")
print("links: " + str(links))

for link in links:
    print("contents: " + str(link.attrs['href']))


#~~~~~~~~~~~~~~~~~~~~~~~~
# Get image from the G-G post URL
#~~~~~~~~~~~~~~~~~~~~~~~~