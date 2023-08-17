import yfinance as yf
import pandas as pd
# Lista de símbolos das ações da Bovespa

symbols = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA', 'B3SA3.SA', 'MGLU3.SA', 'ITSA4.SA',
           'CSNA3.SA', 'LREN3.SA', 'RENT3.SA', 'BBAS3.SA', 'UGPA3.SA', 'IRBR3.SA', 'KLBN11.SA', 'SUZB3.SA',
           'WEGE3.SA', 'CIEL3.SA', 'ELET3.SA', 'FLRY3.SA', 'BRFS3.SA', 'HYPE3.SA', 'RAIL3.SA', 'CVCB3.SA',
           'ENBR3.SA', 'GOLL4.SA', 'CMIG4.SA', 'GOAU4.SA', 'QUAL3.SA', 'CPFE3.SA', 'SBSP3.SA', 'BBSE3.SA',
           'EMBR3.SA', 'ECOR3.SA', 'MYPK3.SA', 'PCAR3.SA', 'HAPV3.SA', 'AMAR3.SA', 'ALSO3.SA', 'KLBN4.SA']
stock_data = {}

# Loop para puxar os dados de cada ação
for symbol in symbols:
    stock_data[symbol] = yf.download(symbol, period="1y")

stock_data.to_csv('acoes.csv')
print(stock_data)
