# #!/usr/bin/env python3

import pandas as pd
import time
import requests
import json
import sys
from io import StringIO
from datetime import datetime
from pandas import json_normalize

start_time = time.time()

data_frames = []

while time.time() - start_time < 1 * 60:
    response = requests.get('https://opendata.api.bb.com.br/open-banking/opendata-exchange/v1/online-rates?page=1&page-size=75')
    print("Status da resposta:", response.status_code, file=sys.stderr)

    if response.status_code == 200:
        json_data = json.loads(response.text)
        data_list = json_data['data']
        for item in data_list:
            item['lastUpdate'] = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        data = json_normalize(data_list)
        data = data[['participant.cnpjNumber', 'foreignCurrency', 'transactionType', 'value', 'valueUpdateDateTime', 'transactionCategory', 'targetAudience', 'lastUpdate']]
        
        data_frames.append(data)  # Adicionar o DataFrame à lista

    time.sleep(5)

# Concatenar todos os DataFrames em um único DataFrame
df = pd.concat(data_frames)

# Remover linhas vazias
df = df.dropna()

# Remove duplicate rows
df = df.drop_duplicates()

# Organizar colunas
df = df.sort_values(['transactionCategory', 'valueUpdateDateTime', 'value', 'foreignCurrency', 'targetAudience'])

csv_data = df.to_csv(mode='a', index=False)

# Configurar o pandas para exibir todas as linhas e colunas
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Imprimir o DataFrame na saída padrão
sys.stdout.write(csv_data)