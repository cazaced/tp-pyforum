# Importation des classes nécessaires
from time import sleep
from pyforum.bd import BD
from pyforum.utilisateur import Utilisateur
from pyforum.forum import Forum
from pyforum.publication import Publication
from pyforum.commentaire import Commentaire
import datetime

def afficher_menu():
    """Affiche les options du menu."""
    print("\n---- Menu ----")
    print("1. Créer un utilisateur")
    print("2. Créer un forum")
    print("3. Créer une publication")
    print("4. Ajouter un commentaire à une publication")
    print("5. Joindre un forum")
    print("6. Quitter")


def main():
    bd = BD()  # Initialisation de la base de données

    while True:
        afficher_menu()
        utilisateurs = []
        forums = []
        # Demander à l'utilisateur de choisir une option
        choix = input("Choisissez une option (1-6): ")

        if choix == '1':
            # Créer un utilisateur
            print("\nCréation d'un utilisateur...")
            username = input("Entrez le nom d'utilisateur: ")
            email = input("Entrez l'adresse e-mail: ")
            mot_de_passe = input("Entrez le mot de passe: ")

            nouvel_id = bd.utilisateurs[-1].identifiant + 1 if bd.utilisateurs else 1
            utilisateur = Utilisateur(nouvel_id, username, email, mot_de_passe)
            bd.sauvegarder_utilisateur(utilisateur)
    

        elif choix == '2':
            # Créer un forum
            print("\nCréation d'un forum...")
            nom_forum = input("Entrez le nom du forum: ")
            description = input("Entrez la description du forum: ")

            nouvel_id = bd.forums[-1].identifiant + 1 if bd.forums else 1
            forum = Forum(nouvel_id, nom_forum, description)
            bd.sauvegarder_forum(forum)

        elif choix == '3':
            # Créer une publication
            print("\nCréation d'une publication...")
            titre = input("Entrez le titre de la publication: ")
            contenu = input("Entrez le contenu de la publication: ")
            auteur_nom = input("Entrez le nom de l'auteur: ")
            forum_nom = input("Entrez le nom du forum: ")

            auteur = bd.obtenir_utilisateur_par_nom(auteur_nom)
            forum = bd.obtenir_forum_par_nom(forum_nom)

            if auteur and forum:
                nouvel_id = bd.publications[-1].identifiant + 1 if bd.publications else 1
                date_creation = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                publication = Publication(nouvel_id, titre, contenu, date_creation, auteur.identifiant, forum.identifiant)
                bd.sauvegarder_publication(publication)
                forum.publications.append(publication.identifiant)
                bd.sauvegarder_forum(forum)
            else:
                print("Auteur ou forum introuvable. Veuillez vérifier les informations saisies.")


        elif choix == '4':
            # Ajouter un commentaire
            print("\nAjouter un commentaire...")
            contenu_commentaire = input("Entrez le contenu du commentaire: ")
            auteur_nom = input("Entrez le nom de l'auteur: ")
            titre_publication = input("Entrez le titre de la publication: ")

            auteur = bd.obtenir_utilisateur_par_nom(auteur_nom)
            publication = bd.obtenir_publication_par_titre(titre_publication)

            if auteur and publication:
                nouvel_id = bd.commentaires[-1].identifiant + 1 if bd.commentaires else 1
                commentaire = Commentaire(nouvel_id, contenu_commentaire, auteur.identifiant, publication.identifiant)
                bd.sauvegarder_commentaire(commentaire)
                publication.ajouter_commentaire(commentaire.identifiant)
                bd.sauvegarder_publication(publication)
            else:
                print("Auteur ou publication introuvable. Veuillez vérifier les informations saisies.")

        elif choix == '5':
            # Joindre un forum
            print("\nJoindre un forum...")
            utilisateur_nom = input("Entrez le nom de l'utilisateur: ")
            forum_nom = input("Entrez le nom du forum: ")

            utilisateur = bd.obtenir_utilisateur_par_nom(utilisateur_nom)
            forum = bd.obtenir_forum_par_nom(forum_nom)

            if utilisateur and forum:
                utilisateur.rejoindre_forum(forum.identifiant)
                bd.sauvegarder_utilisateur(utilisateur)
                print(f"{utilisateur.nom_utilisateur} a rejoint le forum {forum.nom}.")
            else:
                print("Utilisateur ou forum introuvable. Veuillez vérifier les informations saisies.")

        elif choix == '6':
            # Quitter le programme
            print("\nMerci d'avoir utilisé PyForum. À bientôt!")
            break

        else:
            print("Option invalide. Veuillez essayer à nouveau.")

        sleep(2)  # Pause de 2 secondes pour rendre l'interface plus agréable

if __name__ == "__main__":
    main()       
