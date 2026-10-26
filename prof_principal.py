#!/usr/bin/python3

"""
G Le Rest - 2026
Fichier d'entrée
"""

import sys
from modele.chargement import init_donnees_utilisateurs
from vue.fenetre_intro import Fen_intro
from PySide6.QtWidgets import QApplication


def main():
    """Initialisation et lancement de l'application."""
    # copie les données de ressources dans le dossier .local si besoin
    init_donnees_utilisateurs()
    # création de la fenêtre
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    fenetre = Fen_intro()
    fenetre.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
