#-------------------------------INSTALAR BIBLIOTECAS NO PROMPT DO ANACONDA---------------------------------------------------
#pip install selenium webdriver_manager pandas reportlab plotly PyPDF2

import time
import os
import requests
import pandas as pd
import plotly.graph_objs as go
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import PyPDF2

#----------------------AUTOMAÇÃO PARA BAIXAR PLANILHA COM DADOS FILTRADOS DO STATUS INVEST-----------------------------------------------

# Caminho para o arquivo CSV
caminho_arquivo = r'C:\Users\Samsung\Downloads\statusinvest-busca-avancada.csv'

# Verificar se o arquivo existe e excluí-lo
if os.path.exists(caminho_arquivo):
    os.remove(caminho_arquivo)

# Inicialização do driver do Selenium (no exemplo, o ChromeDriver)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Acessar a URL fornecida
navegador.get("https://statusinvest.com.br/acoes/busca-avancada")

# Localizar os elementos pelos XPaths fornecidos e enviar os valores especificados
#min dividend yield
preco_min_input = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/form/div[4]/div[1]/div/div[2]/div[1]/input')
preco_min_input.clear()
preco_min_input.send_keys('6,00')
#max dy
preco_min_input = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/form/div[4]/div[1]/div/div[2]/div[2]/input')
preco_min_input.clear()
preco_min_input.send_keys('40,00')
#min PL
preco_min_input = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/form/div[4]/div[2]/div/div[2]/div[1]/input')
preco_min_input.clear()
preco_min_input.send_keys('1,00')
#max PL
preco_min_input = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/form/div[4]/div[2]/div/div[2]/div[2]/input')
preco_min_input.clear()
preco_min_input.send_keys('20,00')
#máximo vp
dividend_yield_min_input = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/form/div[4]/div[4]/div/div[2]/div[2]/input')
dividend_yield_min_input.clear()
dividend_yield_min_input.send_keys('1,00')
#minimo vp
p_l_max_input = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/form/div[4]/div[8]/div/div[2]/div[1]/input')
p_l_max_input.clear()
p_l_max_input.send_keys('0,00')
#minimo liquidez corrente
p_l_max_input = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/form/div[4]/div[19]/div/div[2]/div[1]/input')
p_l_max_input.clear()
p_l_max_input.send_keys('1,00')

# Clicar no botão de busca
search_button = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]')
search_button.click()

time.sleep(7)
x_anuncio = navegador.find_element(By.XPATH, '/html/body/div[17]/div/div/div[1]/button/i')
x_anuncio.click()
download_btn = navegador.find_element(By.XPATH, '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a/span')
download_btn.click()

time.sleep(3)
navegador.quit()
