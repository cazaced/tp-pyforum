class Utilisateur:
    def __init__(self, identifiant, nom_utilisateur, adresse_email, mot_de_passe):
        self.identifiant = identifiant
        self.nom_utilisateur = nom_utilisateur
        self.adresse_email = adresse_email
        self.mot_de_passe = mot_de_passe
        self.forums = []

    def rejoindre_forum(self, forum_id):
        if forum_id not in self.forums:
            self.forums.append(forum_id)

    def __str__(self):
        return f"Utilisateur(id={self.identifiant}, nom_utilisateur={self.nom_utilisateur}, adresse_email={self.adresse_email})"
            