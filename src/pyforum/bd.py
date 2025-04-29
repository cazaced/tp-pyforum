import csv
import os
import json

from pyforum.utilisateur import Utilisateur
from pyforum.forum import Forum
from pyforum.publication import Publication
from pyforum.commentaire import Commentaire

DOSSIER_DATA = "data"  # Dossier pour stocker les fichiers de données

class BD:
    def __init__(self):
        self.utilisateurs = []
        self.forums = []
        self.publications = []
        self.commentaires = []
        self.utilisateurs_forums = {}
        print("Base de données initialisée.")
    
    def sauvegarder_utilisateur(self, utilisateur):
        for i, existing_user in enumerate(self.utilisateurs):
            if existing_user.identifiant == utilisateur.identifiant:
                self.utilisateurs[i] = utilisateur  # Mise à jour de l'utilisateur existant
                self._sauvegarder_utilisateurs()  # Sauvegarde des utilisateurs
                print(f"[Simulé] Mise à jour de l'utilisateur: {utilisateur}")
                return
        self.utilisateurs.append(utilisateur)  # Ajout de l'utilisateur s'il n'existe pas
        self._sauvegarder_utilisateurs()  # Sauvegarde des utilisateurs
        print(f"[Simulé] Sauvegarde de l'utilisateur: {utilisateur}")
    
    def sauvegarder_forum(self, forum):
        for i, existing_forum in enumerate(self.forums):
            if existing_forum.identifiant == forum.identifiant:
                self.forums[i] = forum  # Mise à jour du forum existant
                self._sauvegarder_forums()  # Sauvegarde des forums
                print(f"[Simulé] Mise à jour du forum: {forum}")
                return
        self.forums.append(forum)  # Ajout du forum s'il n'existe pas
        self._sauvegarder_forums()  # Sauvegarde des forums
        print(f"[Simulé] Sauvegarde du forum: {forum}")

    def sauvegarder_publication(self, publication):
        for i, existing_publication in enumerate(self.publications):
            if existing_publication.identifiant == publication.identifiant:
                self.publications[i] = publication  # Mise à jour de la publication existante
                self._sauvegarder_publications()  # Sauvegarde des publications
                print(f"[Simulé] Mise à jour de la publication: {publication}")
                return
        self.publications.append(publication)  # Ajout de la publication si elle n'existe pas
        self._sauvegarder_publications()  # Sauvegarde des publications
        print(f"[Simulé] Sauvegarde de la publication: {publication}")

    def sauvegarder_commentaire(self, commentaire):
        for i, existing_commentaire in enumerate(self.commentaires):
            if existing_commentaire.identifiant == commentaire.identifiant:
                self.commentaires[i] = commentaire  # Mise à jour du commentaire existant
                self._sauvegarder_commentaires()  # Sauvegarde des commentaires
                print(f"[Simulé] Mise à jour du commentaire: {commentaire}")
                return
        self.commentaires.append(commentaire)  # Ajout du commentaire s'il n'existe pas
        self._sauvegarder_commentaires()  # Sauvegarde des commentaires
        print(f"[Simulé] Sauvegarde du commentaire: {commentaire}")

    def obtenir_forum_par_nom(self, nom_forum):
        return next((forum for forum in self.forums if forum.nom == nom_forum), None)
    
    def obtenir_utilisateur_par_nom(self, nom_utilisateur):
        return next((utilisateur for utilisateur in self.utilisateurs if nom_utilisateur == nom_utilisateur), None)
    
    def obtenir_publication_par_titre(self, titre_publication):
        return next((publication for publication in self.publications if publication.titre == titre_publication), None)
    

    def _sauvegarder_utilisateurs(self):
        if not os.path.exists(DOSSIER_DATA):
            os.makedirs(DOSSIER_DATA)
        with open(os.path.join(DOSSIER_DATA, "utilisateurs.csv"), "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["identifiant", "nom_utilisateur", "adresse_email", "mot_de_passe"])
            for utilisateur in self.utilisateurs:
                writer.writerow([utilisateur.identifiant, utilisateur.nom_utilisateur, utilisateur.adresse_email, utilisateur.mot_de_passe])

    def _sauvegarder_forums(self):
        if not os.path.exists(DOSSIER_DATA):
            os.makedirs(DOSSIER_DATA)
        with open(os.path.join(DOSSIER_DATA, "forums.csv"), "w", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["identifiant", "nom", "description"])
            for forum in self.forums:
                writer.writerow([forum.identifiant, forum.nom, forum.description])

    def _sauvegarder_publications(self):
        if not os.path.exists(DOSSIER_DATA):
            os.makedirs(DOSSIER_DATA)
        publications_data = {str(pub.identifiant): pub.__dict__ for pub in self.publications}
        with open(os.path.join(DOSSIER_DATA, "publications.json"), "w", encoding="utf-8") as f:
            json.dump(publications_data, f, indent=4)

    def _sauvegarder_commentaires(self):
        if not os.path.exists(DOSSIER_DATA):
            os.makedirs(DOSSIER_DATA)
        commentaires_data = {str(com.identifiant): com.__dict__ for com in self.commentaires}
        with open(os.path.join(DOSSIER_DATA, "commentaires.json"), "w", encoding="utf-8") as f:
            json.dump(commentaires_data, f, indent=4)
