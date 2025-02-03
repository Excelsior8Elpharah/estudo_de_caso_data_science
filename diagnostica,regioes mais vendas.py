# Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
from google.colab import files
uploaded = files.upload()  # Faça upload do arquivo 'sales_data.csv'

dados = pd.read_csv('sales_data.csv')

# Substituir valores nulos
dados.fillna(0, inplace=True)

# Agrupar os dados por região para calcular as vendas totais
vendas_regiao = dados.groupby('Região')['Vendas'].sum().reset_index()

# Ordenar as regiões por maior volume de vendas
vendas_regiao = vendas_regiao.sort_values(by='Vendas', ascending=False)

# Visualizar os dados
plt.figure(figsize=(10, 6))
sns.barplot(data=vendas_regiao, x='Região', y='Vendas', palette='coolwarm')
plt.title('Vendas Totais por Região')
plt.xlabel('Região')
plt.ylabel('Total de Vendas')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
