import pandas as pd
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base_dir, '..', 'data', 'consommation_boissons.csv'), sep=';')

# Combien de combinaisons possibles de (boisson × moment de la journée) ?
nb_boissons = df['boisson'].nunique()
nb_moments = df['moment_journee'].nunique()
combinaisons = nb_boissons * nb_moments
print(f"Combinaisons possibles de (boisson × moment de la journée) : {combinaisons}")