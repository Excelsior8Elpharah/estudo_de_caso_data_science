import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
from google.colab import files
uploaded = files.upload()  # Faça upload do arquivo "sales_data.csv"

# Ler os dados
dados = pd.read_csv('sales_data.csv')

# Converter a coluna 'Data' para datetime
dados['Data'] = pd.to_datetime(dados['Data'])

# Preencher valores nulos
dados['Vendas'] = dados['Vendas'].fillna(0)

# Adicionar colunas úteis
dados['Ano'] = dados['Data'].dt.year
dados['Mês'] = dados['Data'].dt.month_name()
dados['Dia_da_Semana'] = dados['Data'].dt.day_name()

# Agrupar os dados por dia da semana, categoria e região
vendas_por_dia_categoria_regiao = dados.groupby(['Dia_da_Semana', 'Categoria', 'Região'])['Vendas'].count().reset_index()

# Ordenar os dias da semana
dias_ordenados = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
vendas_por_dia_categoria_regiao['Dia_da_Semana'] = pd.Categorical(vendas_por_dia_categoria_regiao['Dia_da_Semana'], categories=dias_ordenados, ordered=True)
vendas_por_dia_categoria_regiao = vendas_por_dia_categoria_regiao.sort_values('Dia_da_Semana')

# Visualizar os dados
plt.figure(figsize=(14, 7))
sns.barplot(data=vendas_por_dia_categoria_regiao, x='Dia_da_Semana', y='Vendas', hue='Categoria', palette='viridis')
plt.title('Quantidade de Produtos Vendidos por Categoria e Dia da Semana', fontsize=16)
plt.xlabel('Dia da Semana', fontsize=12)
plt.ylabel('Total de Vendas', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Categoria')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Análise por região
plt.figure(figsize=(14, 7))
sns.barplot(data=vendas_por_dia_categoria_regiao, x='Dia_da_Semana', y='Vendas', hue='Região', palette='magma')
plt.title('Quantidade de Produtos Vendidos por Região e Dia da Semana', fontsize=16)
plt.xlabel('Dia da Semana', fontsize=12)
plt.ylabel('Total de Vendas', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Região')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()