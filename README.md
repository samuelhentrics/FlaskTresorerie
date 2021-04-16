# flaskTresorerie

Ce projet Python utilisant Flask a pour but de gérer les finances d'une mairie grâce à un site.

    Petite information, demain après-midi*, je vais importer la BDD sur GitHub.
    Pour information, il faudra un profil nommé "admin" avec le mdp : "info"
    mais surtout, il faudra crée une database nommé "tresorerie" afin de
    l'importer dedans afin que tout fonctionne parfaitement. 

    *Soit le 17/04/2021 vers 16h/17h

# Dernière mise à jour (16/04/2021)
- Possibilité de modifier l'avatar de son propre profil depuis "Mon Profil" (code non optimal mais fonctionnel)
- L'avatar se met automatiquement en mode "carré" si l'image n'est pas adaptée
- Menu déroulant mis à jour (calendrier uniquement lorsque connecté)

# Comment importer le projet sur une autre machine ?
    Bientôt disponible

# Information dev
    /!\ Début modification page "Mon Profil"
    Au vu du temps que le code pour les avatars prend, nous allons nous
    reconcentrer sur l'emprunt, la caf et la page modification utilisateurs
    à partir du 18/04/2021

    Le 17/04/2021, les finitions de cette partie seront effectués (boutons,
    mise en page...)

**Reste à faire :**

**Emprunts**
  - Emprunts simulation

**CAF**
  - Faire fonctionner le code sans avoir à mettre au début UNE année dans la CAF

**Fonctionnalités profil**
  - Avatar : modifier mise en page (bouton) et ajouter des avatars par defauts.
  - Modifier le mot de passe
  - Edit pour la liste des profils
  -
        Les fonctionnalités supplémentaires tel que les avatars seront déjà
        réalisées sur la page Mon Profil pour être plus tard mise dans liste
        des profils


**Autres**
 - Mettre le plus de messages vers le fichier py/messages.py 
    afin d'éviter de devoir tout modifier dans certaines conditions
    
**Bugs à régler**
  - Les avatars ne se mettent pas à jour directement (problème de cache ?
    uniquement en localhost ?) (résolution le temps de, aller sur le lien de
    l'image et rafraichir)

# Anciennes mises à jour

    Mise à jour du 15/04/2021
        - Amélioration du code permettant de récupérer les emprunts d'une
        année (--> detail_annee.html.jinja)
        - Modification de "mon profil" fonctionnel (sauf mot de passe)

    Mise à jour du 14/04/2021
        - Ajout du logo
        - Suppression des fichiers inutiles
        - Modification des repertoires
        - CAF fonctionnel (modifier, ajouter, supprimer)