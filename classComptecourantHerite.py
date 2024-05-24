import MonMain 
# Classe CompteCourant hérite de Compte et implémente la méthode retirer
class CompteCourant(Compte):
    def __init__(self, titulaire, solde=0):
        super().__init__(titulaire, solde)  
# Appel du constructeur de la classe parent

 # Surcharge de la méthode retirer aux CompteCourant
    def retirer(self, montant):
        if montant <= self._solde:
            self._solde =self._solde - montant
            return self._solde
        return "impossible de retirer car le montant est inferieur au solde" 