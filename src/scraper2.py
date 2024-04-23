import requests
from bs4 import BeautifulSoup
import csv

# URL do site
url = "https://ocacesso.com/#/diagnostico"

# Obter o conteúdo da página
response = requests.get(url)
html_content = response.content

# Analisar o conteúdo HTML
soup = BeautifulSoup(html_content, "html.parser")

# Encontrar todos os elementos <body> com classe específica
site = soup.prettify()

print(site)
# # Encontrar todos os elementos <span> com a classe específica
# titles = soup.find_all("span", class_="text-lg font-bold leading-5 lg:text-xl")

# # Lista para armazenar os títulos
# titles_list = []

# # Extrair os textos dos títulos e adicioná-los à lista
# for title in titles:
#     titles_list.append(title.text.strip())

# # Escrever os títulos em um arquivo CSV
# with open("titles.csv", "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Title"])
#     for title in titles_list:
#         writer.writerow([title])

# print("Os títulos foram extraídos e salvos no arquivo 'titles.csv'.")
