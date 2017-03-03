from bs4 import BeautifulSoup
import requests
import datetime

url = "variety.com"
r = requests.get("http://" + url)
now_time = datetime.datetime.now()

data = r.text

soup = BeautifulSoup(data, 'html5lib')

outfile = open("variety-articles.md", 'a')

date_string = "# Articles scraped at {} #\n".format(now_time)
outfile.write(date_string)

# Stories are <article> with class story
for article in soup.find_all('article', 'story'):
    # The title of the story is contained in an a in an h2
    try:
        article_title = article.h2.a.string
        outfile.write('* ' + article_title + '\n')
    except AttributeError:
        # page has a bunch of empty tags at the bottom, skip these
        pass

outfile.write('\n')

outfile.close()





