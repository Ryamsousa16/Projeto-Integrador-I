from matplotlib.patches import Wedge
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, MonthLocator
from datetime import datetime

data = pd.read_csv('Dados Históricos - Ibovespa.csv') #dataset
data['Data'] = data['Data'].apply(lambda x: datetime.strptime(x, '%d.%m.%Y')) #padronizar a data

#salvando as colunas importantes
dates = data['Data']
close_prices = data['Último']*1000

plt.figure(figsize=(15, 9))  # Define o tamanho do gráfico

month_locator = MonthLocator(interval=3)
month_format = DateFormatter("%d/%m/%Y")  # Formato de data

plt.gca().xaxis.set_major_locator(month_locator)
plt.gca().xaxis.set_major_formatter(month_format)

#pegando a mínima no período inteiro
min_close_date = data.loc[data['Último'].idxmin()]['Data']
min_close_value = data['Último'].min()*1000

#Pegando a máxima no período inteiro
max_close_date = data.loc[data['Último'].idxmax()]['Data']
max_close_value = data['Último'].max()*1000

#definindo as legendas e título do gráfico
plt.plot(dates, close_prices, label='Índice Ibovespa', color='blue')  # Cria um gráfico de linha
plt.xlim(data['Data'].min(), data['Data'].max()) # Delimitando as datas do gráfico
plt.xlabel('Data em trimestre')
plt.ylabel('Pontos do índice ibovespa')  # Define o rótulo do eixo y
plt.title('Variação do ibovespa 1 ano antes da pandemia até fim de 2022')  # Define o título do gráfico

plt.vlines(x=min_close_date, ymin=80000, ymax=min_close_value-5000, color='red', linestyle='-',
           label=f'Mínima no período {min_close_date.strftime("%d/%m/%Y")} aos {min_close_value:.2f} pontos')

plt.vlines(x=max_close_date, ymin=120000, ymax=max_close_value+5000, color='green', linestyle='-',
           label=f'Máxima no período {max_close_date.strftime("%d/%m/%Y")} aos {max_close_value:.2f} pontos')

plt.legend()
plt.tight_layout()  # Melhora o espaçamento entre elementos

# Exibe o gráfico
plt.show()