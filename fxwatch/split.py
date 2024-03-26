#!/usr/bin/env python3

import pandas as pd

# Carregar os dados do arquivo
df = pd.read_csv('fetchout.csv')

# Obter a lista única de categorias
categories = df['transactionCategory'].unique()

# Para cada categoria, criar um novo DataFrame e salvar em um arquivo CSV
for category in categories:
    df_category = df[df['transactionCategory'] == category]
    df_category.to_csv(f'{category}.csv', index=False)