"""
Fenêtre d'accueil 
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QScrollArea)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from pathlib import Path
import json, sqlite3
from modele.choix_chemin_ressources import chemin_ressources
from modele.construction_BDD import ConstructionBDD
from vue.fenetre_principale import Fen_principale
#from controleur.controleur_zone_gauche import ControleurZoneGauche

class Fen_intro(QWidget):
    """Fenêtre de choix de l'organisme"""

    def __init__(self):
        super().__init__()
        self.interface()

    def interface(self) -> None:
        """Création de l'interface graphique"""
        #Fenêtre
        self.resize(380,430)
        self.setWindowTitle("Prof Principal")
        self.setStyleSheet("background-color:white;")
        #Layout principal
        layout=QVBoxLayout()
        layout.setContentsMargins(30,20,60,30)
        layout.setSpacing(12)
        #Titre
        label=QLabel("Introduction")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color:#2F4F4F;font-weight:bold;font-size:20px;")
        layout.addWidget(label)
        # Zone RGPD
        texte_rgpd = (
            "<b>Protection des données</b><br><br>"
            "Ce logiciel traite des données personnelles d'élèves.<br><br>"
            "Son utilisation est soumise au Règlement général "
            "sur la protection des données (RGPD).<br><br>"
            "Le traitement de ces données s'inscrit dans le cadre "
            "défini par l'établissement scolaire.<br><br>"
        )

        label_rgpd = QLabel(texte_rgpd)
        label_rgpd.setWordWrap(True)
        label_rgpd.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        label_rgpd.setMargin(20)
        label_rgpd.setFixedHeight(200)

        label_rgpd.setStyleSheet("""
            QLabel {
                background-color: #f9f9f9;
                color: black;
                font-size: 12px;
                border: 1px solid #999;
            }
        """)

        layout.addWidget(label_rgpd)
        #Bouton OK
        bouton=QPushButton("OK")
        bouton.setFixedWidth(80)
        bouton.setStyleSheet("""
            QPushButton{
                background-color:#76aeba;
                color:white;
                border-radius:12px;
                padding:5px 1px;
                font-weight:bold;
            }
            QPushButton:hover{
                background-color:#66a0b0;
            }""")
        bouton.clicked.connect(self.lancer_prof_principal)
        layout.addWidget(bouton,alignment=Qt.AlignCenter)
        #Logo
        label_logo=QLabel()
        chemin_logo=chemin_ressources("ressources/fichiers/images/prof_principal.png")
        pixmap=QPixmap(str(chemin_logo))
        if not pixmap.isNull():
            label_logo.setPixmap(pixmap.scaledToWidth(90,Qt.SmoothTransformation))
        label_logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(label_logo)
        #Application du layout
        self.setLayout(layout) 

    def lancer_prof_principal(self) -> None:
            """Lancé après le clic utilisateur"""
            # chemin de ~/.loval/principal
            APP_NAME = "prof_principal"
            USER_BASE = Path.home() / ".local" / APP_NAME
            # Chemin COMPLET vers la base de données
            chemin_bdd = USER_BASE / "BaseDonnee" / "eleves.db"
            chemin_CSV = USER_BASE / "fichiers_CSV"
            construction_BDD = ConstructionBDD(chemin_bdd, chemin_CSV)
            # on utilise la connexion de contruction_BDD
            conn = construction_BDD.connexion  
            # Lancement de la fenêtre principale
            self.fenetre_principale = Fen_principale(conn)
            self.fenetre_principale.show()
            self.close() # fermer la fenêtre d'introduction
