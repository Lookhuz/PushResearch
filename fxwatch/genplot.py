import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import sys

# Nome do arquivo passado como argumento de linha de comando
filename = sys.argv[1]

# Carregar os dados do arquivo
data = pd.read_csv(filename)

# Converter 'valueUpdateDateTime' para datetime
data['valueUpdateDateTime'] = pd.to_datetime(data['valueUpdateDateTime'])

# Criar uma nova figura e um conjunto de subplots
fig, ax = plt.subplots(figsize=(10, 5))

# Plotar os dados para cada combinação de transactionType e targetAudience
for transaction_type in ['COMPRA', 'VENDA']:
    for target_audience in ['PESSOA_NATURAL', 'PESSOA_JURIDICA']:
        subset = data[(data['transactionType'] == transaction_type) & (data['targetAudience'] == target_audience)]
        ax.plot(subset['valueUpdateDateTime'], subset['value'], label=f"{transaction_type} - {target_audience}")

# Set the titles of the axes
ax.set_xlabel('TimeStamp')
ax.set_ylabel('Value')

# Definir o título do gráfico
ax.set_title(f"Value Over Time ({filename})")

# Definir a legenda
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1))

# Increase the number of x-axis ticks
ax.xaxis.set_major_locator(ticker.MaxNLocator(16))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

# Increase the number of y-axis ticks
ax.yaxis.set_major_locator(ticker.MaxNLocator(16))

# Rotate x ticks
plt.xticks(rotation=50)

# Mostrar o gráfico
plt.grid(True)
plt.tight_layout()
plt.show()

# dir_path = '/home/usuario/imagens/'
# plt.savefig(f"{dir_path}{filename}.jpg")
