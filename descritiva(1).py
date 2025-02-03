import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
from google.colab import files
uploaded = files.upload()  # Faça upload de um arquivo "sales_data.csv"

dados = pd.read_csv('sales_data.csv')

# Preparação
dados['Data'] = pd.to_datetime(dados['Data'])  # Converter datas
dados['Vendas'] = dados['Vendas'].fillna(0)  # Substituir valores nulos
dados['mes'] = dados['Data'].dt.to_period('M')  # Criar coluna de meses

# Exploração
resumo = dados.groupby(['mes', 'Categoria'])['Vendas'].sum().reset_index()

# Visualizar os dados com gráfico de linhas
plt.figure(figsize=(12, 6))  # Aumenta o tamanho da figura

for categoria in dados['Categoria'].unique():
    subset = resumo[resumo['Categoria'] == categoria]
    plt.plot(subset['mes'].astype(str), subset['Vendas'], label=categoria, marker='o', alpha=0.7)

plt.title('Evolução das Vendas por Categoria')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.legend()
plt.xticks(rotation=50)
plt.grid(True)
plt.tight_layout()  # Ajusta o layout para evitar sobreposição de texto
plt.show()
