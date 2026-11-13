'''
modele de la zone gauche
'''

from modele.gestionnaire_BDD import GestionnaireBDD

class ModeleZoneGauche:

    def __init__(self, connecteur_bdd):
        self.conn = connecteur_bdd
        self.gestionnaire_BDD = GestionnaireBDD(self.conn)

    def recuperer_classes(self) -> list:
        """récupérer la liste des classes"""
        classes = self.gestionnaire_BDD.lister_classes()
        return classes
    
    def recuperer_eleves(self, classe_selectionnee) -> list:
        """recuperer la liste des élèves"""
        return self.gestionnaire_BDD.lister_eleves(classe_selectionnee)

                       