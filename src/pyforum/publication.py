class Publication:
    def __init__(self, identifiant, titre, contenu, date_creation, auteur_id, forum_id):
        self.identifiant = identifiant
        self.titre = titre
        self.contenu = contenu
        self.date_creation = date_creation
        self.auteur_id = auteur_id
        self.forum_id = forum_id
        self.commentaires = []


    def ajouter_commentaire(self, commentaire_id):
        if commentaire_id not in self.commentaires:
            self.commentaires.append(commentaire_id)

    
    def __str__(self):
        return f"Publication(id={self.identifiant}, titre={self.titre}, auteur_id={self.auteur_id}, forum_id={self.forum_id}, commentaires={self.commentaires})"