class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

    def __str__(self):
        return f"Livre: {self.titre} par {self.auteur}, ISBN: {self.isbn}"


class Bibliothèque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Livre ajouté: {livre}")

    def supprimer_livre(self, isbn):
        self.livres = [livre for livre in self.livres if livre.isbn != isbn]
        print(f"Livre avec ISBN {isbn} a été supprimé.")

    def emprunter_livre(self, isbn):
        for livre in self.livres:
            if livre.isbn == isbn:
                print(f"Livre emprunté: {livre}")
                return livre
        print("Livre non trouvé.")
        return None

    def lister_livres(self):
        for livre in self.livres:
            print(livre)

# Exemple d'utilisation des classes
if __name__ == "__main__":
    # Créer quelques livres
    livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "1234567890")
    livre2 = Livre("1984", "George Orwell", "0987654321")

    # Créer une bibliothèque et ajouter des livres
    bibliothèque = Bibliothèque()
    bibliothèque.ajouter_livre(livre1)
    bibliothèque.ajouter_livre(livre2)

    # Lister les livres
    bibliothèque.lister_livres()

    # Emprunter un livre
    bibliothèque.emprunter_livre("1234567890")

    # Supprimer un livre
    bibliothèque.supprimer_livre("0987654321")

    # Lister les livres à nouveau
    bibliothèque.lister_livres()
