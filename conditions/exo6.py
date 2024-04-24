""" 
Calculer le prix d'un article après l'application d'une remise. L'utilisateur est invité à
entrer le prix initial de l'article et le pourcentage de remise. Ensuite, le programme
calcule le montant de la remise et le prix final après remise. Si le prix final est supérieur
à la moitié du prix initial, les résultats sont affichés.
Sinon, un message d'erreur est affiché indiquant que la remise est trop élevée.

"""

prix = int(input("Veuillez entrer le prix initial de l'article : ")) 
remise = int(input("Veuillez entrer le pourcentage de la remise : "))
montant_remise = prix * (remise/100)
prix_finale = prix - montant_remise
moitie_prix = prix/2
print(f"Le prix de votre article aprés remise est : {prix_finale}" if prix_finale > moitie_prix else "la remise est trop élevée.1" )
