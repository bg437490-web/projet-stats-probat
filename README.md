# Projet de Statistique et Probabilités

# Membres du groupe :
# - Abdou Aziz SAMB
# - Abacar Sadikh GUEYE
Partie 1 : Analyse univariée de la consommation de boissons faite par Abdou Aziz SAMB
Ce Projet de Statistique et Probabilités a pour objectif d'analyser la consommation de boissons faite par les étudiants à l'aide de différentes techniques statistiques. Nous allons utiliser un ensemble de données fictives qui contient des informations sur la consommation de boissons par les étudiants, telles que le type de boisson, la quantité consommée, et l'identifiant de l'étudiant.
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