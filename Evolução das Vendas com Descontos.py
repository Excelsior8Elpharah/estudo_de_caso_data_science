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

# Gráfico de Linha - Evolução das Vendas com Descontos
plt.figure(figsize=(14, 7))
sns.lineplot(data=dados, x='Data', y='Vendas', hue='Desconto', palette='coolwarm')
plt.title('Evolução das Vendas com Descontos', fontsize=16)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Vendas', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()