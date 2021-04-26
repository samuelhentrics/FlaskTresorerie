# flaskTresorerie

Ce projet Python utilisant Flask a pour but de gérer les finances d'une mairie grâce à un site.

        Attention, depuis le 24/04/2021, une nouvelle BDD est disponible veuillez
        la mettre à jour si cela n'est pas déjà fait

# Dernière mise à jour (26/04/2021)

- Possibilité de déconnecter un utilisateur depuis la liste de profil.

# Comment importer le projet sur une autre machine ?

Prérequis :
- Ubuntu 20.04 (recommandé)
- Python 3.9 (recommandé)
- Pycharm 2021.1 (recommandé)
- PHPMyAdmin
- Les fichiers de ce projet

**ETAPE 1 : Créer son projet Flask**
    
- Depuis Pycharm -> File -> New Project -> Flask
- Nommer le projet flaskTresorerie
- Dans ce projet, importer tout le projet disponible sur Github

**ETAPE 2 : Importer la BDD**

- Depuis PHPMyAdmin, "Nouvelle base de données" --> tresorerie --> creer
- Allez dans le repertoire "tresorerie" --> importer --> prendre le fichier tresorerie_db.sql et l'importer
- Si le compte "admin" n'existe pas, il faut le créer avec comme mot de passe "info"
    
**ETAPE 3 : AJOUTER TOUS LES MODULES NECESSAIRES**

- Pour cela rien de plus simple, il suffit de faire cette commande dans le terminal PyCharm :
  
        pip install -r requirements.txt
    
**ETAPE 4 : Lancer le projet !**

- Soit depuis le terminal avec
        
        flask run
- Soit en faisant Maj + F10
# Information dev

**Reste à faire :**

**Emprunts**
  - Emprunts simulation

**CAF**
  - Faire fonctionner le code sans avoir à mettre au début UNE année dans la CAF

**Profils**
  - Bouton admin


# Anciennes mises à jour

Mise à jour du 23/04/2021

        - Les messages d'erreurs des formulaires sont maintenant en français.
        (disponible dans messages.py)
        - Les messages d'app.py ont été mis dans messages.py pour mieux gérer les messages
          d'echecs, de succès.
        - Amélioration modification des utilisateurs
        - Ajout d'un rafraichissement du profil pour chaque page
        - Statut connection / admin disponible dans la liste des profils
        - La sécurité du site a été renforcée
        - Correction d'une erreur de lien vers la page Ajouter une année dans CAF
          (localhost/caf/edit --> localhost/caf/add)
        - Si aucune année existe dans la page CAF, une année s'ajoutera automatiquement lors de
          l'ajout d'un emprunt ou lors de la visite de la page caf (annee par defaut étant celle
          actuelle)
        - Correction affichage boutons page "liste emprunts" et "emprunts"
        - Mise à jour du fichier css light.css (pour bouton suppression)
        - Logo mis à jour pour être vu dans le thême jour
        - Correction du bug qui rafraichissait pas automatiquement les avatars
          (utilisation de timestamps)
        - Modification du mot de passe possible depuis le compte utilisé (page Mon Profil)
        - Modification des avatars possible depuis "Liste des profils"

Mise à jour du 23/04/2021

        - Ajout d'une page erreur 413
        - Les numéros de téléphone sont affichés correctement
        - Amélioration du code confirmation mdp

Mise à jour du 17/04/2021

        - Page "Mon Profil" fonctionnel (hors mot de passe)
        - Possibilité de modifier le mot de passe depuis la page "Liste des profils"
        - MAJ design page edition "Liste des profils"


Mise à jour du 16/04/2021

        - Possibilité de modifier l'avatar de son propre profil depuis "Mon Profil"
        - L'avatar se met automatiquement en mode "carré" si l'image n'est pas adaptée
        - Menu déroulant mis à jour (calendrier uniquement lorsque connecté)


Mise à jour du 15/04/2021

        - Amélioration du code permettant de récupérer les emprunts d'une
        année (--> detail_annee.html.jinja)
        - Modification de "mon profil" fonctionnel (sauf mot de passe)

Mise à jour du 14/04/2021

        - Ajout du logo
        - Suppression des fichiers inutiles
        - Modification des repertoires
        - CAF fonctionnel (modifier, ajouter, supprimer)