# Implantation de la base de données

Un fois le [MVP terminé](../01_MVP/01_Enonce.md), votre travail consiste à
modifier le fichier `bd.py` pour que les données soient enregistrées dans des
fichiers.

**Vous pouvez faire cette partie du travail sans avoir complété la partie 02_GIT**

## Choisir le bon format

Le format de fichier que vous allez utiliser pour enregistrer les données est
important, car il va faciliter (ou pas) la lecture et l'écriture des données.
Si les données sont tabulaires, c'est à dire qu'il serait facile de les
représenter dans Excel, le fichier CSV est probablement un bon choix.

Si au contraire, les données sont plus complexes, il est préférable d'utiliser
un format de fichier plus flexible. Le format de fichier JSON est un bon choix,
car il est facile à lire et à écrire. De plus, tout objet Python peut être
converti assez facilement en dictionnaire Python et tout dictionnaire Python
peut être converti en JSON.

## À vous de jouer !

### Étape 1

Compléter le MVP (partie 01) si ce n'est pas déjà fait.

### Étape 2

Modifier le fichier `bd.py` pour que les données soient enregistrées dans des
fichiers. 
  
Nous vous recommandons de créer un dossier `data` sur votre machine et d'y
enregistrer les fichiers. Ce dossier n'a pas besoin d'être dans le répertoire
`src/pyforum`. Pour faire simple, vous pouvez coder en dur le chemin du dossier
`data` dans le fichier `bd.py`. Nous verrons plus tard comment rendre le
dossier `data` dynamique.