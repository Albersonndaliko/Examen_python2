from classComptEpargneEherite import CompteCourant
from classComptecourantHerite import CompteEpargne
# Utilisation de l'héritage, de la surcharge, du polymorphisme, de l'abstraction et de l'encapsulation
compte1 = CompteCourant("Albert ", 1000)
compte2 = CompteEpargne("ndaliko", 500)

# albert dépose  sur son compte
compte1.deposer(200)

# ndaliko retire  sur son compte épargne
compte2.retirer(100)

# albert fait un virement à ndaliko
compte1.virementSurCompte(300, compte2)

# Affichage des soldes
print(compte1.afficher_solde())  
print(compte2.afficher_solde()) 