"""
Gestion de la langue
"""

import sqlite3, csv

class ConstructionBDD:

    def __init__(self, chemin_bdd, chemin_CSV):
        self.chemin_bdd = chemin_bdd
        self.chemin_CSV = chemin_CSV
        base_a_creer = not chemin_bdd.exists()
        self.connexion = sqlite3.connect(self.chemin_bdd)
        self.curseur = self.connexion.cursor()
        self.curseur.execute("PRAGMA foreign_keys = ON;")
        if base_a_creer:
            self.creation_tables()
            self.remplissage_tables()

    def creation_tables(self) -> None:
        """Création des tables"""

        self.curseur.execute("PRAGMA foreign_keys = ON")
        # Table identites
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS identites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prenom TEXT,
                nom TEXT,
                classe TEXT,
                photo TEXT
            )
        """)
        self.connexion.commit()
        # Table bilans
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS bilans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                trimestre INTEGER,
                appreciation TEXT,
                av_travail INTEGER,
                av_comportement INTEGER,
                encouragements BOOLEAN,
                felicitations BOOLEAN,
                id_eleve INTEGER,
                FOREIGN KEY (id_eleve) REFERENCES identites(id)
                    ON DELETE CASCADE
            )
        """)
        self.connexion.commit()
    
    def remplissage_tables(self)->None:
        """remplissage des tables avec les fichiers CSV"""
        # table "identites"
        chemin_identites = self.chemin_CSV / "identites.csv"
        with open(chemin_identites, newline='', encoding="utf-8") as f:
            lecteur =csv.reader(f)
            next(lecteur) # on saute la première ligne
            for ligne in lecteur:
                nom, prenom, photo, classe = ligne
                self.curseur.execute("""
                INSERT INTO identites(nom, prenom, photo, classe)
                VALUES(?, ?, ?, ?)
                """, (nom, prenom, photo, classe))                
        self.connexion.commit()
        # table "petsonnes_specialites
        chemin_bilan = self.chemin_CSV / "bilans.csv"
        with open(chemin_bilan, newline='', encoding="utf-8") as f:
            lecteur =csv.reader(f)
            next(lecteur) # on saute la première ligne
            for ligne in lecteur:
                id_eleve, trimestre, appreciation, av_travail, av_comportement, encouragements, felicitations = ligne
                self.curseur.execute("""
                INSERT INTO bilans(trimestre, appreciation, av_travail, av_comportement, encouragements, felicitations, id_eleve)
                VALUES(?, ?, ?, ?, ?, ?, ?)
                """, (trimestre, appreciation, av_travail, av_comportement, encouragements, felicitations, id_eleve))
        self.connexion.commit()
