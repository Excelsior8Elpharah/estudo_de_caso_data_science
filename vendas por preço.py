# Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
from google.colab import files
uploaded = files.upload()  # Faça upload do arquivo "sales_data.csv"

# Ler os dados
dados = pd.read_csv('sales_data.csv')

# Converter a coluna de data para o formato datetime
dados['Data'] = pd.to_datetime(dados['Data'])

# Preencher valores nulos
dados['venda ID'] = dados['venda ID'].fillna(0)

# Adicionar colunas úteis para análise
dados['Ano'] = dados['Data'].dt.year
dados['Mês'] = dados['Data'].dt.month_name()
dados['Dia_da_Semana'] = dados['Data'].dt.day_name()

# Visualizar o conjunto de dados inicial
dados.head()

# Definir faixas de preço
faixa_preco = pd.cut(dados['Preço'], bins=[0, 50, 100, 200, 500, 1000, 5000])

# Agrupar vendas por faixa de preço
vendas_por_preco = dados.groupby(faixa_preco)['venda ID'].sum()

plt.figure(figsize=(12, 6))
vendas_por_preco.plot(kind='bar', color='lightsteelblue')
plt.title('Vendas Totais por Faixa de Preço', fontsize=16)
plt.xlabel('Faixa de Preço', fontsize=12)
plt.ylabel('Total de Vendas', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()

