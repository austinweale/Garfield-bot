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

def log_msg(msg):
    print("~~~~~~~~~~~~~~~~~~~~")
    print(msg)
    print("~~~~~~~~~~~~~~~~~~~~")

count = 0

for posts_year in range(2008, 2019):
    for posts_month in range(1, 12):
        log_msg("SEARCHING FOR: " + str(posts_month) + "/" + str(posts_year))
        #Get full page html
        html = urlopen(format_url(posts_year, posts_month))
        html_page = BeautifulSoup(html, 'html.parser')

        #get html for current month's comics
        post_id = format_post_id(posts_year, posts_month)
        current_month_div = html_page.find(id=post_id)
        div_doc = BeautifulSoup(str(current_month_div), 'html.parser')

        links = div_doc.find_all("a")

        for link in links:
            count += 1
            current_link = str(link.attrs['href'])
            print("contents: " + current_link)
            comic_doc = BeautifulSoup(str(current_link), 'html.parser')
            current_month_div = html_page.find(id="content")
            print("current links")

log_msg("TOTAL IMAGES: " + str(count))
#~~~~~~~~~~~~~~~~~~~~~~~~
# Get image from the G-G post URL
#~~~~~~~~~~~~~~~~~~~~~~~~