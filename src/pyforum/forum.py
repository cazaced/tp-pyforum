class Forum:
    def __init__(self, identifiant, nom, description=""):
        self.identifiant = identifiant
        self.nom = nom
        self.description = description
        self.publications = []

    def ajouter_publication(self, publication_id):
        if publication_id not in self.publications:
            self.publications.append(publication_id)


    def __str__(self):
        return f"Forum(id={self.identifiant}, nom={self.nom}, description={self.description}, publications={self.publications})"