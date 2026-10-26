"""
Fenêtre d'accueil – choix de l'organisme :
École, Entreprise, Collectivité
"""
from modele.gestionnaire_BDD import GestionnaireBDD
from PySide6.QtWidgets import QWidget

class Fen_principale(QWidget):
    """Fenêtre de choix de l'organisme"""

    def __init__(self, connecteur_bdd):
        super().__init__()
        self.conn = connecteur_bdd
        self.interface()
        
    def interface(self) -> None:
        """Création de l'interface graphique"""
        #Fenêtre
        self.resize(320,430)
        self.setWindowTitle("Prof principal")
        self.setStyleSheet("background-color:white;")
        self.gestionnaire_bdd = GestionnaireBDD(self.conn)

       