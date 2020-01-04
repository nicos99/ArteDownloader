# ArteDownloader
## *Purpose (English)*
A short python3 script to download easily a replay video from Arte website

## Objectif
Un petit script python3 pour télécharger facilement une vidéo en replay depuis le site Web d'Arte

## *Limitations (English)*
- For the moment, download only the **hight quality french version** of the video (SQ_1).
    - in the future this could be setup by command line switch. 
- Simplest download feature : no kind of optmisation nor recovery in case of failure.
    - For instance I noticed that if the network is lost for too long time, the download can stall for ever.
- Require **Python 3** installed (no compile avalable right now)

## Limitations
- Pour le moment, télécharge uniquement la **version française de haute qualité** de la vidéo (SQ_1).
     - A l'avenir, cela pourrait être configuré par un commutateur de ligne de commande.
- Fonction de téléchargement simplicime : aucune espèce d'optimisation ni système de récupération en cas d'erreur réseau.
     - Par exemple, j'ai remarqué que si le réseau est perdu pendant trop longtemps, le téléchargement peut stagner éternellement.
- Nécessite d'avoir **Python 3** installé (pas de compilation disponible pour le moment)

## Installation
Enregistrez le fichier [ArteDL.py](https://raw.githubusercontent.com/nicos99/ArteDownloader/master/ArteDL.py) sur votre ordinateur (via `CTRL +  S` une fois le script affiché).

## Usage
Parant du principe que vous avez *python* dans le PATH :
- Ouvrez une invite de commande à partir du dossier dans lequel vous voulez télécharger la vidéo :
    - Sous Windows, ouvrez un explorateur (`Win + E`).
    - Naviguez et vers le dossier voulu puis sélectionnner-le par `MAJ + bouton droit` et choisir *Ouvrir une fenêtre de commandes ici* ou *Ouvrir la fenêtre PowerShell ici* dans le menu contextuel.
- Entrez `python `.
- Effectuez un glisser-déposer dans la console de votre ficher 'ArteDL.py' enregistré en local.
- Dans votre navigateur Internet affichez la page de la vidéo à télécharger.
- Copiez le lien partageable à partir du bouton *"Partager"* présent en haut à droite de la vidéo.
- Retourner dans l'invite de commande, ajoutez un espace puis collez le lien (par un `bouton droit`).

Voici ce que cela doit donner par exemple pour un dossier de travail `D:\temp` :  
`D:\temp> python C:\Users\nicos\Downloads\ArteDL.py https://www.arte.tv/fr/videos/083285-001-A/athleticus/`  
Il ne reste plus qu'à valider par \[*Entrer*\] !
