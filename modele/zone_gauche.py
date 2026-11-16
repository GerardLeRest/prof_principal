'''
modele de la zone gauche
'''

from modele.gestionnaire_BDD import GestionnaireBDD

class ModeleZoneGauche:

    def __init__(self, connecteur_bdd, liste_eleves):
        self.conn = connecteur_bdd
        self.liste_eleves = liste_eleves
        self.gestionnaire_BDD = GestionnaireBDD(self.conn)
        self.liste_eleves = liste_eleves
        self.rang = 0

    def recuperer_classes(self) -> list:
        """récupérer la liste des classes"""
        classes = self.gestionnaire_BDD.lister_classes()
        return classes
    
    def recuperer_eleves(self, classe_selectionnee) -> list:
        """ récupérer la liste des élèves """
        self.liste_eleves = self.gestionnaire_BDD.lister_eleves(classe_selectionnee)
        self.rang = 0
        return self.liste_eleves


    def acceder_premier(self) -> None:
        """Accéder au premier élève de la liste"""
        if self.liste_eleves:
            self.rang = 0

    def acceder_precedent(self) -> None:
        """Accéder à l'élève précédent"""
        if self.rang > 0:
            self.rang -= 4
        
    def acceder_suivant(self) -> None:
        """Accéder à l'élève suivant"""
        if self.rang < len(self.liste_eleves) - 1:
            self.rang += 4
        

    def acceder_dernier(self) -> None:
        """Accéder au dernier élève"""
        if self.liste_eleves:
            self.rang = len(self.liste_eleves) - 1
        int(self.rang)