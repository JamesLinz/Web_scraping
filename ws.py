from bs4 import BeautifulSoup

import requests


#objeto site recebendo o conteúdo da requisição http do site em questão...
site = requests.get("https://www.climatempo.com.br/").content

#objeto soup baixando do site o html
soup = BeautifulSoup(site, 'html.parser')

#transforma html em string e o print vai exibir o html
# print(soup.prettify())

temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

# print(temperatura.string)
print(soup.title)
print(soup.find('admin'))