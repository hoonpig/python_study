from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip install beautifulsoup4
# pip list
# pip show package name
# pip uninstall beautifulsopu4