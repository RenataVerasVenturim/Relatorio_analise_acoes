#-------------------------------CÓDIGO COMPILADO-----------------------------------------

#-----------------------------------------------------------GERAR VISUALIZAÇÃO DOS DADOS DA PLANILHA----------------

import requests
import plotly.graph_objs as go
import requests
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import date
import os

# Caminho para o arquivo CSV
caminho_arquivo = r'C:\Users\Samsung\Downloads\statusinvest-busca-avancada.csv'

# Carregar os dados da planilha para um DataFrame do Pandas
dados = pd.read_csv(caminho_arquivo, sep='\t', decimal=',')

# Exibir os dados
print(dados)

time.sleep(3)

# Função para obter os dados da API e criar um gráfico
def obter_dados_e_plotar(ticker):
    # Construir a URL da API com o ticker fornecido
    url = f"https://www.brinvestapi.me/api/all/{ticker}"
    
    # Fazer a requisição à API
    response = requests.get(url)
    
    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Extrair os dados da resposta da API
        dados_api = response.json()
        
        # Extrair os valores desejados
        dates = [item['date'] for item in dados_api]
        close_values = [item['close'] for item in dados_api]
        
        # Criar o gráfico com Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=close_values, mode='lines', name=f'Close - {ticker}'))
        fig.update_layout(title=f'Gráfico de Fechamento para {ticker}',
                          xaxis_title='Data',
                          yaxis_title='Preço de Fechamento')
        
        # Exibir o gráfico
        fig.show()

time.sleep(4)
#---------------------------------------CONSUMIR API COM DADOS DE ABERTURA E FECHAMENTO----------------------------------


# Caminho para o arquivo CSV
caminho_arquivo = r'C:\Users\Samsung\Downloads\statusinvest-busca-avancada.csv'

# Carregar os dados da planilha para um DataFrame do Pandas
dados = pd.read_csv(caminho_arquivo, sep=';')

# Função para obter os dados da API e criar um gráfico
def obter_dados_e_plotar(ticker):
    # URL da API com o ticker da ação
    url = f"https://www.brinvestapi.me/api/all/{ticker}"
    
    # Fazer a requisição à API
    response = requests.get(url)
    
    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Extrair os dados da resposta JSON
        dados_api = response.json()
        
        # Para este exemplo, vou apenas exibir os dados da API
        print(f"Dados para o ticker {ticker}:")
        print(dados_api)
        
        # URL da API para os dados de dividendos
        url_dividend = f"https://www.brinvestapi.me/api/fundamentus/dividend?ticket={ticker}"
        
        # Fazer a requisição à API para os dados de dividendos
        response_dividend = requests.get(url_dividend)
        
        # Verificar se a requisição foi bem-sucedida
        if response_dividend.status_code == 200:
            # Extrair os dados JSON da resposta
            data_dividend = response_dividend.json()
            
            # Extrair os dados de dividendos
            dividend_yield = data_dividend.get('dividendYield')
            if dividend_yield:
                # Extrair a porcentagem de dividendos
                porcentagem_dividendos = dividend_yield.get('porcentage')
                
                # Imprimir os dados de dividendos
                print(f"Porcentagem de dividendos para o ticker {ticker}: {porcentagem_dividendos}")
            else:
                print(f"Dados de dividendos ausentes para o ticker {ticker}")
        else:
            print(f"Erro ao acessar os dados de dividendos para o ticker {ticker}")
    else:
        print(f"Erro ao acessar a API para o ticker {ticker}")

# Iterar sobre cada linha no DataFrame e chamar a função para cada ticker
for index, row in dados.iterrows():
    ticker = row['TICKER']
    obter_dados_e_plotar(ticker)

time.sleep(10)#--------------------------------------GERAR PDF DAS MÉDIAS MÓVEIS -RELATÓRIO ----------------------------------
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import date
import os

# Função para adicionar texto no topo do arquivo PDF
def adicionar_texto_topo(c):
    # Data de hoje
    data_hoje = date.today().strftime("%d/%m/%Y")
    
    # Título do relatório
    titulo = "RELATÓRIO DE AÇÕES"

    # Nome do autor
    #autor = "Criado por Renata Veras Venturim"

    #Seção
    secao="ANÁLISE TÉCNICA"
    # Definir a fonte e o tamanho do texto
    c.setFont("Helvetica-Bold", 16)
    
    # Coordenadas para o texto
    largura, altura = letter
    x = largura / 2
    y = altura - 50

    # Desenhar o texto no topo da página
    c.drawCentredString(x, y, f"{titulo} - {data_hoje}" )
    #c.drawCentredString(x, y - 20, f"{autor}")
    c.drawCentredString(x, y - 40, secao)

# Caminho para o arquivo CSV
caminho_arquivo = r'C:\Users\Samsung\Downloads\statusinvest-busca-avancada.csv'

# Função para obter os dados da API e criar um gráfico
def obter_dados_e_plotar(ticker, c):
    # URL da API com o ticker da ação
    url = f"https://www.brinvestapi.me/api/all/{ticker}"
    
    # Fazer a requisição à API
    response = requests.get(url)
    
    # Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Extrair os dados da resposta JSON
        dados_api = response.json()
        historicalData = dados_api.get('historicalDataPrice')
        if historicalData:
            # Extrair datas e preços de fechamento
            datas = [entry['date'] for entry in historicalData]
            precos_fechamento = [entry['close'] for entry in historicalData]

            # Calcular a média móvel com uma janela de 30 dias
            janela_media_movel = 30
            media_movel = []
            for i in range(len(precos_fechamento) - janela_media_movel + 1):
                media = sum(precos_fechamento[i:i + janela_media_movel]) / janela_media_movel
                media_movel.append(media)

            # Verificar se o preço de fechamento na data mais recente é maior que a média móvel
            if precos_fechamento[-1] > media_movel[-1]:
                # Criar o gráfico apenas se o preço de fechamento for maior que a média móvel
                plt.figure(figsize=(10, 6))
                plt.plot(datas[janela_media_movel - 1:], media_movel, label='Média Móvel (30 dias)', color='red')
                plt.plot(datas, precos_fechamento, label='Preço de Fechamento', color='blue')
                plt.title(f'Gráfico de Preço de Fechamento com Média Móvel para {ticker}')
                plt.xlabel('Data')
                plt.ylabel('Preço')
                plt.legend()
                plt.grid(True)
                plt.savefig(f"{ticker}_grafico.png")  # Salvar o gráfico como imagem

                # Adicionar a imagem ao arquivo PDF
                c.drawImage(f"{ticker}_grafico.png", 50, 100, width=500, height=300)
                os.remove(f"{ticker}_grafico.png")  # Remover a imagem após adicioná-la ao PDF
                c.showPage()  # Avançar para a próxima página

# Criar um arquivo PDF para o relatório
with open('Relatorio_Analise_técnica_Acoes.pdf', 'wb') as f:
    c = canvas.Canvas(f, pagesize=letter)
    
    # Adicionar texto no topo do arquivo PDF
    adicionar_texto_topo(c)

    # Iterar sobre cada linha no DataFrame e chamar a função para cada ticker
    for index, row in dados.iterrows():
        ticker = row['TICKER']
        obter_dados_e_plotar(ticker, c)

    c.save()  # Salvar o arquivo PDF
#-------------------------------------------gera PDF com tabela com relação de ações---------------------------------
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import pandas as pd

# Caminho para o arquivo CSV
caminho_arquivo = r'C:\Users\Samsung\Downloads\statusinvest-busca-avancada.csv'

# Carregar os dados da planilha para um DataFrame do Pandas
dados = pd.read_csv(caminho_arquivo, sep=';')

# Função para adicionar a tabela ao arquivo PDF
def adicionar_tabela_pdf(c, dados):
    # Definir as coordenadas iniciais da tabela
    x_inicial = 50
    y_inicial = 600
    altura_linha = 20

    # Definir a largura das colunas
    largura_colunas = [100, 150, 50, 150]

    # Definir o cabeçalho da tabela
    c.setFont("Helvetica-Bold", 12)
    c.drawString(x_inicial, y_inicial, "TICKER")
    c.drawString(x_inicial + largura_colunas[1], y_inicial, "DY")
    c.drawString(x_inicial + sum(largura_colunas[:1]), y_inicial, "P/L")
    c.drawString(x_inicial + sum(largura_colunas[:2]), y_inicial, "VP")

    # Definir a fonte para o corpo da tabela
    c.setFont("Helvetica", 10)

    # Iterar sobre as linhas da planilha para adicionar os dados à tabela
    y_atual = y_inicial - altura_linha
    for index, row in dados.iterrows():
        y_atual -= altura_linha
        c.drawString(x_inicial, y_atual, str(row['TICKER']))
        c.drawString(x_inicial + largura_colunas[1], y_atual, str(row['DY']))
        c.drawString(x_inicial + sum(largura_colunas[:1]), y_atual, str(row['P/L']))
        c.drawString(x_inicial + sum(largura_colunas[:2]), y_atual, str(row['P/VP']))

# Criar um arquivo PDF para o relatório
with open('Relatorio_Analise_Fundamentalista_Acoes.pdf', 'wb') as f:
    c = canvas.Canvas(f, pagesize=letter)
    
    # Adicionar texto no topo do arquivo PDF
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "RELATÓRIO - Análise Fundamentalista de Ações")

    # Adicionar a tabela ao arquivo PDF
    adicionar_tabela_pdf(c, dados)

    c.showPage()  # Avançar para a próxima página
    c.save()  # Salvar o arquivo PDF

#----------------------------------------------juntar PDFS e gerar o relatório consolidado----------------
import PyPDF2

# Arquivos a serem combinados
arquivo1 = "Relatorio_Analise_Fundamentalista_Acoes.pdf"
arquivo2 = "Relatorio_Analise_técnica_Acoes.pdf"  # Nome do arquivo que está na mesma pasta

# Nome do arquivo PDF consolidado
arquivo_consolidado = "Relatório_Consolidado_acoes.pdf"

# Abrir os arquivos PDF
with open(arquivo1, "rb") as file1, open(arquivo2, "rb") as file2:
    # Criar objetos PDF para os arquivos
    pdf1 = PyPDF2.PdfReader(file1)
    pdf2 = PyPDF2.PdfReader(file2)

    # Criar um objeto PDF para o arquivo consolidado
    pdf_writer = PyPDF2.PdfWriter()

    # Adicionar páginas do primeiro arquivo
    for page_num in range(len(pdf1.pages)):
        pdf_writer.add_page(pdf1.pages[page_num])

    # Adicionar páginas do segundo arquivo
    for page_num in range(len(pdf2.pages)):
        pdf_writer.add_page(pdf2.pages[page_num])

    # Salvar o arquivo consolidado
    with open(arquivo_consolidado, "wb") as output_file:
        pdf_writer.write(output_file)

print(f"Arquivos combinados com sucesso em '{arquivo_consolidado}'.")

