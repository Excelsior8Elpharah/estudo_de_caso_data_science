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

dados['Ano'] = dados['Data'].dt.year
dados['Mês'] = dados['Data'].dt.month_name()
dados['Dia_da_Semana'] = dados['Data'].dt.day_name()

# Agrupar os dados por dia da semana, categoria e região
vendas_por_dia_categoria_regiao = dados.groupby(['Dia_da_Semana', 'Categoria', 'Região'])['Vendas'].sum().reset_index()

# Ordenar os dias da semana
dias_ordenados = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
vendas_por_dia_categoria_regiao['Dia_da_Semana'] = pd.Categorical(vendas_por_dia_categoria_regiao['Dia_da_Semana'], categories=dias_ordenados, ordered=True)
vendas_por_dia_categoria_regiao = vendas_por_dia_categoria_regiao.sort_values('Dia_da_Semana')



# Heatmap - Impacto dos Descontos por Região
descontos_regiao = dados.pivot_table(values='Vendas', index='Região', columns='Desconto', aggfunc='sum')
plt.figure(figsize=(12, 6))
sns.heatmap(descontos_regiao, cmap='magma', annot=True, fmt='.0f')
plt.title('Impacto dos Descontos nas Vendas por Região', fontsize=16)
plt.xlabel('Faixa de Desconto', fontsize=12)
plt.ylabel('Região', fontsize=12)
plt.show()
