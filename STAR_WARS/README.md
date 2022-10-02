Installation
--------------------------------------------------------------
Tout d'abord, il faut installer Python et votre IDE. 

<u>Rappel</u> : Veuillez vérifier que Python est bien présent dans les variables d'environnement de votre système.
Pour ce faire, ouvrer votre outil de recherche windows à l'aide de la touche ```Win```, puis entrez 
"Modifier les variables d'environnement système". Vous devez ensuite vous rendre dans la catégorie variable 
d'environnement et vous n'avez plus qu'à vérifier si elles sont présentes pour Python.

Dorénavant, votre environnement de travail est mis en place. Voici ci-dessous les différentes étapes à suivre pour 
pouvoir réutiliser ce projet :

Tout d'abord, il faut importer le projet dans votre IDE.
Ensuite, il faut mettre en place l'environnement de travail pour python.

### Commandes Importantes

<u>Facultatif</u> : Activer l'environnement Python
```shell
pip install virtualenv
virtualenv venv
# Windows CMD
venv\Scripts\activate.bat
#Windows Powershell
venv\Scripts\activate.ps1
# Linux/MacOS
source venv/bin/activate
```
Et pour désactiver votre environnement de travail (même commande pour tous les systèmes) :
```shell
deactivate
```

Lancer le projet
```shell
python main.py
```

* Pour générer la documentation html (avec Sphinx) : 
```shell
cd docs
sphinx-apidoc -o .\source\ ..\
sphinx-build -b html .\source\  html
```

Ensuite rendez-vous dans "docs\html" et lancez le fichier "index.html", afin de pouvoir visualiser la documentation.