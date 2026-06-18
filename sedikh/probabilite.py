# ============================================================
# Projet3 : Analyse des Habitudes de Consommation de Boissons
# Partie : PROBABILITE
# ============================================================
# Questions traitées (sujet Projet 3) :
#   - P(boire du café)
#   - P(consommer le matin)
#   - P(boire du jus | température > 30°C)
#   - P(consommation élevée (>3 verres) | étudiant masculin)

import pandas as pd
# ------------------------------------------------------------
# 0. CHARGEMENT DES DONNEES
# ------------------------------------------------------------
df = pd.read_csv("../data/consommation_boissons.csv", sep=";")
print(df.head())
# ------------------------------------------------------------
# 1. P(BOIRE DU CAFE)
# ------------------------------------------------------------
p_cafe = (df["boisson"] == "Café Touba").mean()
print(f"P(boire du café) = {p_cafe:.2f}")
# ------------------------------------------------------------
# 2. P(CONSOMMER LE MATIN)
# ------------------------------------------------------------
p_matin = (df["moment_journee"] == "matin").mean()
print(f"P(consommer le matin) = {p_matin:.2f}")
# ------------------------------------------------------------
# 3. P(BOIRE DU JUS | TEMPERATURE > 30°C)
temp_chaude = df[df["temperature"] > 30]
p_jus_temp_chaude = (temp_chaude["boisson"].str.contains("Jus")).mean()
print(f"P(boire du jus | température > 30°C) = {p_jus_temp_chaude:.2f}")
# ------------------------------------------------------------
# 4. P(CONSOMMATION ELEVEE (>3 VERRES) | ETUDIANT MASCULIN)
etudiant_masculin = df[(df["sexe"] == "M") & (df["quantite"] >= 3)]
p_consommation_elevee_masculin = len(etudiant_masculin) / (df["sexe"] == "M").sum()
print(f"P(consommation élevée (>3 verres) | étudiant masculin) = {p_consommation_elevee_masculin:.2f}")
