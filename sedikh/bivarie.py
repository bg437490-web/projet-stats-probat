# ============================================================
# PROJET 3 - ANALYSE DES HABITUDES DE CONSOMMATION DE BOISSONS
# Partie : ANALYSE BIVARIEE
# ============================================================

# Questions traitées (sujet Projet 3) :
#   1. Moment de la journée vs type de boisson
#   2. Température élevée vs consommation
#   3. Sexe vs type de boisson préféré
#   4. Âge vs quantité consommée

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 0. CHARGEMENT DES DONNEES
# --------------------------------------------
df = pd.read_csv("../data/consommation_boissons.csv", sep=";")
print(df.head())
# ------------------------------------------------------------
# 1. MOMENT DE LA JOURNEE VS TYPE DE BOISSON
# ------------------------------------------------------------
moment_boisson = pd.crosstab(df["moment_journee"], df["boisson"])
print(f"Moment de la journée vs Type de boisson :\n{moment_boisson}")
sns.heatmap(moment_boisson, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Moment de la journée vs Type de boisson")
plt.xlabel("Type de boisson")
plt.ylabel("Moment de la journée")
plt.show()
# ------------------------------------------------------------
# 2. TEMPERATURE ELEVE vs CONSOMMATION
# ------------------------------------------------------------
df["temperature_eleve"] = df["temperature"].apply(lambda x: "Elevée" if x > 25 else "Normale")
temp_consommation = pd.crosstab(df["temperature_eleve"], df["quantite"])
print(f"Température élevée vs Consommation :\n{temp_consommation}")
sns.heatmap(temp_consommation, annot=True, fmt="d", cmap="YlOrRd")
plt.title("Température élevée vs Consommation")
plt.xlabel("Consommation")
plt.ylabel("Température élevée")
plt.show()
# ------------------------------------------------
# 3. SEXE vs TYPE DE BOISSON PREFERE
# ------------------------------------------------
sexe_boisson = pd.crosstab(df["sexe"], df["boisson"])
print(f"Sexe vs Type de boisson préféré :\n{sexe_boisson}")
sns.heatmap(sexe_boisson, annot=True, fmt="d", cmap="PuBuGn")
plt.title("Sexe vs Type de boisson préféré")
plt.xlabel("Type de boisson préféré")
plt.ylabel("Sexe")
plt.show()
# ------------------------------------------------
# 4. AGE vs QUANTITE CONSOMMEE
age_consommation = df[["age", "quantite"]]
print(f"Âge vs Quantité consommée :\n{age_consommation.head()}")
sns.scatterplot(data=age_consommation, x="age", y="quantite")
plt.title("Âge vs Quantité consommée")
plt.xlabel("Âge")
plt.ylabel("Quantité consommée")
plt.show()


