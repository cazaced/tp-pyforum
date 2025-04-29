class Commentaire:
    def __init__(self, identifiant, auteur_id, contenu, publication_id):
        self.identifiant = identifiant
        self.auteur_id = auteur_id
        self.contenu = contenu
        self.publication_id = publication_id


    def __str__(self):
        return f"Commentaire(id={self.identifiant}, auteur_id={self.auteur_id}, contenu={self.contenu}, publication_id={self.publication_id})"