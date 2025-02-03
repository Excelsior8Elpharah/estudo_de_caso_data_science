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

plt.figure(figsize=(10, 6))
sns.scatterplot(data=dados, x='Desconto', y='venda ID', hue='Categoria', palette='coolwarm', alpha=0.7)
sns.regplot(data=dados, x='Desconto', y='venda ID', scatter=False, color='red', ci=None, line_kws={"linestyle": "--"})
plt.title('Relação entre Desconto e Vendas', fontsize=16)
plt.xlabel('Desconto (%)', fontsize=12)
plt.ylabel('Total de Vendas', fontsize=12)
plt.grid(alpha=0.3)
plt.show()

