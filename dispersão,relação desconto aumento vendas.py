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

# Criar gráfico de dispersão para visualizar a relação entre descontos e vendas
plt.figure(figsize=(10, 6))
sns.scatterplot(data=dados, x='Desconto', y='venda ID', hue='Categoria', palette='viridis', alpha=0.7)

# Adicionar uma linha de tendência
sns.regplot(data=dados, x='Desconto', y='venda ID', scatter=False, color='red', ci=None, line_kws={"linestyle": "--"})

# Configurações do gráfico
plt.title('Relação entre Descontos e Vendas')
plt.xlabel('Desconto (%)')
plt.ylabel('Total de Vendas')
plt.legend(title='Categoria', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(alpha=0.3)
plt.show()
