# Projet de Statistique et Probabilités

# Membres du groupe :
# - Abdou Aziz SAMB
# - Abacar Sedikh GUEYE
# Projet 3 : ANALYSE DES HABITUDES DE CONSOMMATION DE BOISSONS
Ce Projet de Statistique et Probabilités a pour objectif d'analyser la consommation de boissons faite par les étudiants à l'aide de différentes techniques statistiques. Nous allons utiliser un ensemble de données fictives qui contient des informations sur la consommation de boissons par les étudiants, telles que le type de boisson, la quantité consommée, et l'identifiant de l'étudiant.

# - Partie 1 : Analyse univariée et Dénombrement  faite par Abdou Aziz SAMB
# Importation des bibliothèques nécessaires
import pandas as pd
import matplotlib.pyplot as plt
# Chargement des données
df = pd.read_csv('consommation_boisson.csv')
je viens de terminer l'analyse univariée de la consommation de boissons faite par les étudiants. Voici les étapes que j'ai suivies :
1. J'ai chargé les données à partir d'un fichier CSV et j'ai vérifié les premières lignes pour m'assurer que les données sont correctement chargées.
2.J'ai calculé le boison le plus consommé en utilisant la fonction `value_counts()` pour compter les occurrences de chaque type de boisson.
3. J'ai créé un graphique à barres pour visualiser la consommation de chaque type de boisson.
4. J'ai trouvé la distribution des quantités consommées en utilisant un histogramme.
5. J'ai calculé la consommation moyenne par étudiant en regroupant les données par identifiant d'étudiant et en calculant la moyenne des quantités consommées.
Je viens de terminer le fichier de denombrement. ce fichier contient les resultats suivants :
-Combien de combinaisons possibles(boisson * moment de la journée) : 15
-Combien de façons différentes un étudiant peut consommer 3 boissons dans une journée : 10
-Profils possibles (âge, sexe, boisson, moment) : 240

# - Partie 2 : Analyse Bivarié et Probabilité faite par Ababacar Sedikh Gueye
# Importation des bibliothèques nécessaires
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1 Analyse Bivariée (bivarie.py)
Cette section explore les relations et corrélations entre deux variables du fichier à l'aide de tableaux croisés (pd.crosstab) :Moment de la journée vs Type de boisson : Analyse des préférences de consommation selon les heures (matin, midi, soir), visualisée par une carte thermique (sns.heatmap).Température élevée vs Consommation : Transformation de la variable continue temperature en catégories (Elevée si > 25 vs Normale) croisée avec la colonne réelle quantite pour observer l'impact de la chaleur sur le nombre de verres bus.Sexe vs Type de boisson préféré : Analyse comparative des choix de boissons entre les profils hommes (M) et femmes (F), illustrée par une heatmap.Âge vs Quantité consommée : Observation de la tendance de consommation selon l'âge des étudiants (de 18 à 26 ans), représentée par un nuage de points (sns.scatterplot).

# 2 Calculs de Probabilités (probabilite.py)
Ce script calcule des pourcentages simples et des pourcentages avec conditions, directement basés sur les lignes de notre fichier :Pour le café (0.21) : Cela veut dire que 21 % des boissons choisies dans tout le fichier sont du Café Touba (environ 2 étudiants sur 10).Pour le matin (0.29) : Cela signifie que 29 % des consommations ont lieu le matin.Pour le jus quand il fait chaud (0.15) : C'est un calcul ciblé. Si on prend uniquement les moments où il fait plus de 30 degré, le jus représente 15 % des choix.Pour la grosse consommation chez les garçons (0.03) : C'est une condition sur le sexe. Si on regarde uniquement le groupe des garçons, seuls 3 % d'entre eux boivent une grande quantité (3 verres ou plus). C'est donc très rare dans notre fichier.


projet-stats-probat/
│
├── data/
│   └── consommation_boissons.csv   # Fichier de données source (séparateur ";")
│
├── sedikh/
│   ├── bivarie.py                 # Script de génération des tableaux croisés et heatmaps
│   └── probabilite.py             # Script des calculs de probabilités conditionnelles
│
├── abdou/
│   ├── univarie.py                # Script d'analyse univariée et histogrammes
│   └── denombrement.py            # Script des calculs combinatoires
│
├── venv/                          # Environnement virtuel Python et dépendances
└── README.md                      # Documentation du projet