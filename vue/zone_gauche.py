'''
# fenetre de la zone gauche
'''
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QSizePolicy
from modele.gestionnaire_BDD import GestionnaireBDD
from PySide6.QtCore import Qt

class ZoneGauche(QWidget):

    def __init__(self, connecteur_bdd):
        super().__init__()
        self.conn = connecteur_bdd
        self.interface()

    def interface(self):
        """interface de la zone gauche"""
        layout_principal=QHBoxLayout()
        # label Classe
        label_classe = QLabel("Classe")
        layout_principal.addWidget( label_classe, alignment=Qt.AlignTop | Qt.AlignHCenter)
        label_classe.setStyleSheet("color: #76aeba; font-weight: bold; font-size: 16px")
        # Combobox pour la saisie de la classe
        self.comboBox = QComboBox()
        self.comboBox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.comboBox.setMinimumHeight(32)
        # textes du combobox
        gestionnaire_BDD = GestionnaireBDD(self.conn)
        classes = gestionnaire_BDD.lister_classes()
        self.comboBox.addItems(classes)
        # Connexion du signal
        self.comboBox.currentTextChanged.connect(self.afficher_classe_selectionnee)
        # ajout du combobox
        layout_principal.addWidget(self.comboBox)
        # attacher le layout à la zone
        self.setLayout(layout_principal)
        

    def afficher_classe_selectionnee(self, texte: str) -> None:
        """ initialise les variables du combobox """
        print("classe sélectionnée:", texte)
