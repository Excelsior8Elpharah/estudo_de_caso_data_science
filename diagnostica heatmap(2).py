# Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
from google.colab import files
uploaded = files.upload()  # Faça upload do arquivo 'sales_data.csv'

dados = pd.read_csv('sales_data.csv')

# Converter datas
dados['Data'] = pd.to_datetime(dados['Data'])

# Substituir valores nulos
dados.fillna(0, inplace=True)

# Criar uma matriz de análise apenas com colunas relevantes
colunas_relevantes = ['Produto', 'Categoria', 'Região', 'Preço', 'Quantidade']
dados_filtrados = dados[dados['Produto'].isin(['Produto A', 'Produto B', 'Produto C', 'Produto D']) |
                        dados['Categoria'].isin(['Eletrônicos', 'Roupas', 'Casa', 'Livros']) |
                        dados['Região'].isin(['Norte', 'Sul', 'Leste', 'Oeste'])]

# Converter categorias para numérico
dados_filtrados['Produto'] = dados_filtrados['Produto'].astype('category').cat.codes
dados_filtrados['Categoria'] = dados_filtrados['Categoria'].astype('category').cat.codes
dados_filtrados['Região'] = dados_filtrados['Região'].astype('category').cat.codes

# Criar matriz de correlação
correlacao = dados_filtrados[['Produto', 'Categoria', 'Região', 'Preço', 'Quantidade']].corr()

# Criar heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Heatmap de Correlação entre Produtos, Categorias, Região, Preço e Quantidade')
plt.show()
