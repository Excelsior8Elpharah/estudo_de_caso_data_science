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

# Vendas totais por mês
vendas_mensais = dados.groupby('Mês')['venda ID'].sum()

plt.figure(figsize=(12, 6))
vendas_mensais.plot(kind='line', marker='o', color='mediumblue', linestyle='-', linewidth=2)
plt.title('Vendas Totais por Mês', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Total de Vendas', fontsize=12)
plt.grid(alpha=0.3)
plt.xticks(rotation=45)
plt.show()
