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

# Agrupar os dados para encontrar os produtos mais vendidos por categoria
produtos_vendidos = dados.groupby(['Categoria', 'Produto'])['Quantidade'].sum().reset_index()

# Encontrar o produto mais vendido por categoria
top_produtos = produtos_vendidos.loc[produtos_vendidos.groupby('Categoria')['Quantidade'].idxmax()]

# Visualizar os dados
plt.figure(figsize=(12, 6))
sns.barplot(data=top_produtos, x='Categoria', y='Quantidade', hue='Produto', palette='viridis')
plt.title('Produtos Mais Vendidos por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.legend(title='Produto')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
