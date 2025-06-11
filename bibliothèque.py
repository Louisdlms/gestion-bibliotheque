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

def afficher_menu():
    print("\nMenu:")
    print("1. Ajouter un livre")
    print("2. Supprimer un livre")
    print("3. Lister les livres")
    print("4. Emprunter un livre")
    print("5. Quitter")

def main():
    bibliothèque = Bibliothèque()

    while True:
        afficher_menu()
        choix = input("Choisis une option (1-5): ")

        if choix == "1":
            titre = input("Titre du livre: ")
            auteur = input("Auteur du livre: ")
            isbn = input("ISBN du livre: ")
            livre = Livre(titre, auteur, isbn)
            bibliothèque.ajouter_livre(livre)

        elif choix == "2":
            isbn = input("ISBN du livre à supprimer: ")
            bibliothèque.supprimer_livre(isbn)

        elif choix == "3":
            bibliothèque.lister_livres()

        elif choix == "4":
            isbn = input("ISBN du livre à emprunter: ")
            bibliothèque.emprunter_livre(isbn)

        elif choix == "5":
            print("Au revoir!")
            break

        else:
            print("Option non valide, veuillez choisir une option entre 1 et 5.")

if __name__ == "__main__":
    main()
