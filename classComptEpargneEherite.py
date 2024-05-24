from MonMain import Compte
class CompteEpargne(Compte):
    def __init__(self, titulaire, solde=0):
        super().__init__(titulaire, solde)  
# Appel du constructeur de la classe parent

# Surcharge de la méthode retirer pour le CompteEpargne avec une vérification de solde minimum
    def retirer(self, montant):
        if montant <= self._solde and self._solde - montant >= 0:  
# Solde minimum de 50 après retrait
            self._solde -= montant
            return "reussi avec succes"
        return "operation a echouer"