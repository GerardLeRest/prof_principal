'''
Controleur de la zone gauche
récupération listes de classe et des élèves
'''

from modele.modele_zone_gauche import ModeleZoneGauche

class ControleurZoneGauche:

    def __init__(self,connecteur_bdd ):
        self.conn = connecteur_bdd
        self.modele_zone_gauche = ModeleZoneGauche(self.conn)

    def recuperer_classes(self) -> list:
       return self.modele_zone_gauche.recuperer_classes()

    def recuperer_eleves(self, classe_selectionnee) -> list:
        return self.modele_zone_gauche.recuperer_eleves(classe_selectionnee)
        