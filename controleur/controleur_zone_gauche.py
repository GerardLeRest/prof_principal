'''
Controleur de la zone gauche
récupération listes de classe et des élèves
'''

from modele.zone_gauche import ModeleZoneGauche
from PySide6.QtCore import Slot

class ControleurZoneGauche:

    def __init__(self, connecteur_bdd, vue_zone_gauche):
        self.conn = connecteur_bdd
        self.vue_zone_gauche = vue_zone_gauche
        self.modele_zone_gauche = ModeleZoneGauche(self.conn, vue_zone_gauche.liste_eleves)
        vue_zone_gauche.demande_avancer.connect(self.avancer)
        vue_zone_gauche.demande_reculer.connect(self.reculer)
        vue_zone_gauche.demande_debut.connect(self.debut)
        vue_zone_gauche.demande_fin.connect(self.fin)

    def recuperer_classes(self) -> list:
       return self.modele_zone_gauche.recuperer_classes()

    def recuperer_eleves(self, classe_selectionnee) -> list:
        if classe_selectionnee == "-- Choisir une classe --": # ne tient pas compte de cette ligne
            return
        return self.modele_zone_gauche.recuperer_eleves(classe_selectionnee)
    
    def avancer(self) -> None:
        """Avancer d'un rang"""
        self.modele_zone_gauche.acceder_suivant()
        self.vue_zone_gauche.rang = self.modele_zone_gauche.rang
        self.vue_zone_gauche.mise_a_jour_globale()

    @Slot()
    def reculer(self) -> None:
        """Reculer vers la gauche."""
        self.modele_zone_gauche.acceder_precedent()
        self.vue_zone_gauche.rang = self.modele_zone_gauche.rang
        self.vue_zone_gauche.mise_a_jour_globale()

    @Slot()
    def debut(self) -> None:
        """Aller au début."""
        self.modele_zone_gauche.acceder_premier()
        self.vue_zone_gauche.rang = self.modele_zone_gauche.rang
        self.vue_zone_gauche.mise_a_jour_globale()

    @Slot()
    def fin(self) -> None:
        """Aller à la fin."""
        self.modele_zone_gauche.acceder_dernier()
        self.vue_zone_gauche.rang = self.modele_zone_gauche.rang
        self.vue_zone_gauche.mise_a_jour_globale()


        