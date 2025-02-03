# Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
from google.colab import files
uploaded = files.upload()  # Faça upload do arquivo 'sales_data.csv'

dados = pd.read_csv('sales_data.csv')

# Converter a coluna 'Data' para datetime
dados['Data'] = pd.to_datetime(dados['Data'])

# Criar uma coluna com o dia da semana
dados['Dia_da_Semana'] = dados['Data'].dt.day_name()

# Agrupar os dados por dia da semana e somar as vendas
vendas_por_dia = dados.groupby('Dia_da_Semana')['venda ID'].sum().reset_index()

# Ordenar os dias da semana na ordem correta
dias_ordenados = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
vendas_por_dia['Dia_da_Semana'] = pd.Categorical(vendas_por_dia['Dia_da_Semana'], categories=dias_ordenados, ordered=True)
vendas_por_dia = vendas_por_dia.sort_values('Dia_da_Semana')

# Visualizar os dados
plt.figure(figsize=(10, 6))
sns.barplot(data=vendas_por_dia, x='Dia_da_Semana', y='venda ID', palette='mako')
plt.title('Volume de Vendas por Dia da Semana')
plt.xlabel('Dia da Semana')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
