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

# Agrupar vendas por faixa de desconto
faixa_desconto = pd.cut(dados['Desconto'], bins=[0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 100])
vendas_por_desconto = dados.groupby(faixa_desconto)['venda ID'].sum()

plt.figure(figsize=(12, 6))
vendas_por_desconto.plot(kind='bar', color='lightcoral')
plt.title('Vendas por Faixa de Desconto', fontsize=16)
plt.xlabel('Faixa de Desconto (%)', fontsize=12)
plt.ylabel('Total de Vendas', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.show()


