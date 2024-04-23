from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import math

# URL do site que você deseja raspar
url = "https://ocacesso.com/#/diagnostico/medicina-nuclear"

# HEADERS
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"}

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get(url)

time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')





# # Fazendo a solicitação HTTP
# response = requests.get(url, headers=headers)

# # Verificando se a solicitação foi bem-sucedida
# if response.status_code == 200:
#     # Analisando o conteúdo da página com BeautifulSoup
#     soup = BeautifulSoup(response.content, 'html.parser')
    
#     # Aqui você pode extrair as informações que deseja do site.
#     # Por exemplo, vamos supor que você queira extrair todos os títulos <h1>:
#     h1_tags = soup.find_all('h1')
#     titles = [tag.text for tag in h1_tags]
    
#     # Criando um DataFrame com os títulos
#     df = pd.DataFrame(titles, columns=['Título'])
    
#     # Salvando o DataFrame em um arquivo Excel
#     df.to_excel('titulos.xlsx', index=False)
# else:
#     print("Não foi possível acessar o site.")
