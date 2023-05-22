import requests
from bs4 import BeautifulSoup

# Scrape Musk's Twitter page
response = requests.get('https://twitter.com/elonmusk')
soup = BeautifulSoup(response.content, 'html.parser')

# Find all tweet links
links = []
for link in soup.find_all('a'):
    if '/status/' in link.get('href'):
        links.append('https://twitter.com' + link['href'])

# Write links to file
with open('links.txt', 'w') as f:
    for link in links:
        f.write(link + '\n')
