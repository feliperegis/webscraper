from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import csv

# Configurando o serviço do Microsoft Edge WebDriver
edge_driver_path = "C:\\Users\\fereg\\Downloads\\edgedriver_win64"  # Substitua pelo caminho do seu msedgedriver
service = Service(edge_driver_path)
service.start()

# Configurando o navegador Microsoft Edge
options = webdriver.EdgeOptions()
options.use_chromium = True  # Use o modo Chromium para suportar a versão mais recente do Edge
options.add_argument("--headless")  # Execução em modo headless (sem janelas visíveis)
driver = webdriver.Edge(service=service, options=options)

# URL do site
url = "https://ocacesso.com/#/diagnostico"

# Carregar a página
driver.get(url)

# Encontrar todos os elementos <span> com a classe específica
titles = driver.find_elements(By.CSS_SELECTOR, "span.text-lg.font-bold.leading-5.lg\\:text-xl")

# Lista para armazenar os títulos
titles_list = []

# Extrair os textos dos títulos e adicioná-los à lista
for title in titles:
    titles_list.append(title.text.strip())

# Escrever os títulos em um arquivo CSV
with open("titles.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title"])
    for title in titles_list:
        writer.writerow([title])

print("Os títulos foram extraídos e salvos no arquivo 'titles.csv'.")

# Fechar o navegador
driver.quit()
