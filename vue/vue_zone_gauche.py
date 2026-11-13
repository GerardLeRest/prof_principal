'''
# fenetre de la zone gauche
'''
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QSizePolicy, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtGui import QPixmap, QIcon
import sys
from pathlib import Path
# Ajoute la racine du projet au chemin Python (2 lignes suivantes)
dossier_racine = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(dossier_racine))
from controleur.controleur_zone_gauche import ControleurZoneGauche

icones = [
    "bouton_debut.png",
    "bouton_precedent.png",
    "bouton_suivant.png",
    "bouton-fin.png"
]

class ZoneGauche(QWidget):

    # signaux
    demande_avancer = Signal()
    demande_reculer = Signal()
    demande_debut = Signal()
    demande_fin = Signal()

    def __init__(self, connecteur_bdd):
        super().__init__()
        self.conn = connecteur_bdd
        self.controleur_zone_gauche = ControleurZoneGauche(self.conn)
        self.rang = 0 # rang de l'élève
        self.nbre_eleves = 0 # nbre des élèves dans la classe
        self.interface()
        self.rang = 0 # rang de l'élève
        self.nbre_eleves = 0 # nbre des élèves dans la classe

    def interface(self):
        """interface de la zone gauche"""
        self.layout_principal=QVBoxLayout()
        self.interface_haute()
        self.interface_basse()
        # attacher le layout à la zone
        self.setLayout(self.layout_principal)
        
    def recuper_eleves_classe(self, classe_selectionnee: str) -> None:
        """ récuperation de la liste des élèves et leurs données"""
        eleves = self.controleur_zone_gauche.recuperer_eleves(classe_selectionnee)
        print(eleves)

    def interface_haute(self)-> None:
        """ affichage Classe et combobox"""
        # label Classe
        label_classe = QLabel("Classe")
        self.layout_principal.addWidget( label_classe, alignment=Qt.AlignTop | Qt.AlignHCenter)
        label_classe.setStyleSheet("color: #76aeba; font-weight: bold; font-size: 16px")
        # Combobox pour la saisie de la classe
        self.comboBox = QComboBox()
        self.comboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.comboBox.setMinimumHeight(32)
        # lignes du combobox
        classes = self.controleur_zone_gauche.recuperer_classes()
        classes.insert(0, "-- Choisir une classe --")
        self.comboBox.addItems(classes)
        # Connexion du signal
        self.comboBox.currentTextChanged.connect(self.recuper_eleves_classe)
        # ajout du combobox
        self.layout_principal.addWidget(self.comboBox, alignment=Qt.AlignTop | Qt.AlignHCenter)

    def interface_basse(self) -> None:
        """afficher l'image, le prénom et le nom"""
        # image
        # Création du QLabel de l'image
        self.label_image = QLabel()
        self.label_image.setFixedSize(128, 128)
        # self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_image.setStyleSheet("border: 1px solid #666; background-color: #f0f0f0;")
        # Chargement de l'image par défaut
        chemin_defaut = dossier_racine / "ressources" / "fichiers" / "images" / "inconnu.jpg"
        pixmapDefaut = QPixmap(str(chemin_defaut)).scaled(
            128, 128,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.label_image.setPixmap(pixmapDefaut)
        self.layout_principal.addWidget(self.label_image, alignment=Qt.AlignTop | Qt.AlignHCenter)
        # prénom et nom
        label_prenom_nom = QLabel("Nom Prénom")
        self.layout_principal.addWidget( label_prenom_nom, alignment=Qt.AlignTop | Qt.AlignHCenter)
        label_prenom_nom.setStyleSheet("color: #76aeba; font-weight: bold; font-size: 16px")
        # boutons et N° élèves
        layout_boutons = QHBoxLayout()
        bouton_debut = QPushButton()
        bouton_debut.setIcon(QIcon(str(dossier_racine / "ressources" / "fichiers" / "icones" / "bouton_debut.png")))
        bouton_debut.setIconSize(QSize(24, 24))
        bouton_debut.clicked.connect(self.demande_debut.emit)
        layout_boutons.addWidget(bouton_debut)
        # bouton précédent
        bouton_reculer = QPushButton()
        bouton_reculer.setIcon(QIcon(str(dossier_racine / "ressources" / "fichiers" / "icones" / "bouton_precedent.png")))
        bouton_reculer.setIconSize(QSize(24, 24))
        bouton_reculer.clicked.connect(self.demande_reculer.emit)
        layout_boutons.addWidget(bouton_reculer)
        # rang/nbre_élèves
        self.rang_nbre_eleves = QLabel(str(self.rang) + " / " + str(self.nbre_eleves))
        layout_boutons.addWidget(self.rang_nbre_eleves, alignment=Qt.AlignTop | Qt.AlignHCenter)
        # bouton suivant
        bouton_avancer = QPushButton()
        bouton_avancer.setIcon(QIcon(str(dossier_racine / "ressources" / "fichiers" / "icones" / "bouton_suivant.png")))
        bouton_avancer.setIconSize(QSize(24, 24))
        bouton_avancer.clicked.connect(self.demande_avancer.emit)
        layout_boutons.addWidget(bouton_avancer)
        # bouton fin
        bouton_fin = QPushButton()
        bouton_fin.setIcon(QIcon(str(dossier_racine / "ressources" / "fichiers" / "icones" / "bouton_fin.png")))
        bouton_fin.setIconSize(QSize(24, 24))
        bouton_fin.clicked.connect(self.demande_fin.emit)
        layout_boutons.addWidget(bouton_fin)
        # permet de traiter les quatre à la fois (activer/desactiver)
        self.boutons = [bouton_debut, bouton_reculer, bouton_avancer, bouton_fin]
        layout_boutons.setSpacing(6)  # espace horizontal entre flèches
        self.layout_principal.addLayout(layout_boutons)
