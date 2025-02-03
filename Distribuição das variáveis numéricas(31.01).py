import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import files

# Upload do arquivo CSV
uploaded = files.upload()

# Carregar o arquivo CSV
file_name = list(uploaded.keys())[0]
df = pd.read_csv(file_name)

# Exibir as primeiras linhas do dataset
print("Visualização inicial dos dados:")
display(df.head())

# Informações gerais sobre os dados
df.info()

# Verificar valores ausentes
print("\nValores ausentes:")
print(df.isnull().sum())

# Estatísticas descritivas
display(df.describe())


# Histogramas para cada coluna numérica
df.hist(figsize=(12, 8), bins=30, edgecolor='black')
plt.suptitle("Distribuição das variáveis numéricas")
plt.show()