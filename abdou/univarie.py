import pandas as pd
import matplotlib.pyplot as plt

# Chargement des données
df = pd.read_csv("../data/consommation_boissons.csv", sep=';')
print(df.head())

# Quelles sont les boissons les plus consommées ?
print(df['boisson'].value_counts())
# la boisson la plus consommée.
boisson_max = df['boisson'].value_counts().idxmax()
print("Boisson la plus consommée :", boisson_max)

# Visualisation de la boisson la plus consommée
plt.figure(figsize=(8, 6))
df['boisson'].value_counts().plot(kind='bar', color='skyblue')
plt.xlabel('Boisson')
plt.ylabel('Nombre de consommations')
plt.title('Distribution des consommations de boissons')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()