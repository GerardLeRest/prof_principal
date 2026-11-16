"""
Fenêtre d'accueil – choix de l'organisme :
École, Entreprise, Collectivité
"""
from modele.gestionnaire_BDD import GestionnaireBDD
from vue.zone_gauche import ZoneGauche
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget

class Fen_principale(QMainWindow):
    """Fenêtre de choix de l'organisme"""

    def __init__(self, connecteur_bdd):
        super().__init__()
        self.conn = connecteur_bdd
        self.gestionnaire_bdd = GestionnaireBDD(self.conn)
        self.liste_eleves = self.gestionnaire_bdd.liste_eleves
        self.liste_classes = self.gestionnaire_bdd.liste_classes
        self.interface()
        
    def interface(self) -> None:
        """Création de l'interface graphique."""
        self.resize(250, 375)
        self.setWindowTitle("Prof principal")
        self.setStyleSheet("background-color:white;")
        # Widget central
        # QMainWindow ne permet pas d'installer directement un layout avec self.setLayout()
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        # Layout principal
        layout_principal = QHBoxLayout()
        # Zone gauche
        self.zone_gauche = ZoneGauche(self.conn)
        layout_principal.addWidget(self.zone_gauche)
        # Association du layout au widget central
        widget_central.setLayout(layout_principal)      