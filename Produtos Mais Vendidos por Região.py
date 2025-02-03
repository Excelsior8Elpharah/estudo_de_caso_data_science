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

# Vendas por produto e região
vendas_produto_regiao = dados.groupby(['Produto', 'Região'])['venda ID'].sum().unstack()

vendas_produto_regiao.plot(kind='bar', stacked=False, figsize=(12, 6), colormap='viridis')
plt.title('Produtos Mais Vendidos por Região', fontsize=16)
plt.xlabel('Produto', fontsize=12)
plt.ylabel('Vendas', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.show()





