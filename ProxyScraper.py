# NEEDS PIP INSTALL 'bs4'

import requests
from bs4 import BeautifulSoup

proxyDomain = "https://free-proxy-list.net/"
r = requests.get(proxyDomain)
soup = BeautifulSoup(r.content, "html.parser")
table = soup.find('table',{"id":"proxylisttable"})

for row in table.find_all('tr'):
    columns = row.find_all('td')
    try:
        print("Proxy = %s : %s \t Anominity = %s \t Country = %s : %s \t\t Https = %s" % (columns[0].get_text(), columns[1].get_text(), columns[4].get_text(), columns[3].get_text(), columns[2].get_text(), columns[6].get_text()))
    except:
        print("\n")
