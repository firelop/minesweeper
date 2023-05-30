# Démineur
Le démineur est un jeu popularisé par le système d'exploitation Windows. En effet celui-ci était intégré gratuitement dans windows.
Le jeux se compose d'une grille de taille différente celon la difficulté. Le principe du jeu est très simple: placer un drapeau sur chaque bombe.
Vous cliquerez sur une case:
- Si celle-ci est une bombe: vous perdez la partie.
- Si celle-ci n'est pas une bombe: un nombre s'afficher. Ce nombre indique le nombre de bombes présente dans les 8 cases limitrophes.

## Présentation du projet
Cette version du démineur est le travail de 3 étudiants (Nolan Appert, Leon Guennec, Pierre Guchet) dans le lycée [https://www.saintaubinlasalle.fr](saint-aubin la salle).
![Logo saint-aubin la salle](https://www.staubinlasalle.fr/wp-content/uploads/2022/06/cropped-cropped-logo-final-1.1.png)
Il est réalisé dans le cadre de la spécialité NSI 1ère.

## Télécharger et jouer
### Télécharger
Il existe deux manières possibles pour télécharger le projet.

#### Via git
Ouvrez un terminal là où vous souhaiter télécharger le projet.
Executer la commande:
```BASH
git clone https://github.com/firelop/minesweeper.git
```

#### En fichier zip
Vous pouvez aussi télécharger une archive zip du projet en cliquant [ici](https://github.com/firelop/minesweeper/archive/refs/heads/master.zip)
Il vous suffit ensuite d'en extraire le contenu dans le dossier que vous souhaitez.

### Installer les dépendances
Ouvrez un terminal à la racine du projet puis executez:
```BASH
pip install -r requirements.txt
```
### Jouer
Ouvrez un terminal à la racine du projet puis executez:
```BASH
python game.py
```


