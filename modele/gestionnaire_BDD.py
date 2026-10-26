""" 
récupération des données de la base de donnée 
"""

import sqlite3


class GestionnaireBDD:
    """Création de la liste des élèves"""

    def __init__(self, connexion_bdd: sqlite3.Connection):
        """
        Initialise la classe avec une connexion SQLite déjà ouverte.
        """
        self.connexion_bdd = connexion_bdd
        self.curseur = self.connexion_bdd.cursor()
        # classe traitée
        self.classe = ""
        # Activer les clés étrangères (important avec SQLite)
        self.curseur.execute("PRAGMA foreign_keys = ON;")
        # Liste des élèves chargés
        self.liste_eleves = []
        self.liste_classes = []
        # Chargement des élèves
        self.liste_eleves = self.charger_eleves("PSTI")
        print (self.liste_eleves)
        print(" ")
        # chargement des classes
        self.liste_classes = self.charger_classes()
        print (self.liste_classes)

    def charger_eleves(self, classe:str)-> list:
        """
        Charge les eleves d'une classe depuis la base de données et
        les stocke dans self.liste_eleves.
        """
        self.liste_eleves.clear()
        self.curseur.execute("""
            SELECT 
                i.prenom,
                i.nom,
                i.classe,
                i.photo,
                b.trimestre,
                b.appreciation,
                b.av_travail,
                b.av_comportement,
                b.encouragements,
                b.felicitations                
            FROM identites i
            LEFT JOIN bilans b
            ON i.id = b.id_eleve
            WHERE i.classe = ?
        """, (classe,))
        # liste de tuples
        # [("Lucas", "Dupont", "TSTI1", "lucas.jpg", "Bon trimestre", 0, 0, 1, 0),
        # ("Emma", "Martin", etc...)
        for (prenom, nom, classe,
             photo, trimestre, appreciation,
             av_travail, av_comportement,
             encouragements, felicitations,) in self.curseur.fetchall():
            eleve = [
                prenom,
                nom, 
                classe,
                photo,
                trimestre,
                appreciation,
                av_travail,
                av_comportement,
                encouragements,
                felicitations,
            ]
            self.liste_eleves.append(eleve)
        return self.liste_eleves

    def charger_classes(self) -> list:
        """
        Charge les classes depuis la base de données et
        les stocke dans self.liste_classes.
        """
        self.liste_classes.clear()
        self.curseur.execute("""
            SELECT DISTINCT i.classe
            FROM identites i
            """)
        for classe in self.curseur.fetchall():
            une_classe = classe[0]
            self.liste_classes.append(une_classe)
        return self.liste_classes

    def fermer_connexion(self)-> None:
        """
        Ferme proprement la connexion à la base de données.
        """
        self.connexion_bdd.close()
