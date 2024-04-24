""" 
Afin d’utiliser les conditions imbriquées, créer une histoire avec 3 niveaux minimum avec
au minimum 3 fins différentes vous devez faire des “if” imbriqués. Vous devez utiliser la
fonction “input()”. Aucune autre fonction n’est autorisée. Bien entendu une des fins doit
obligatoirement finir par “La grande réponse sur la vie, l’univers et le reste !”.
Utilisez “print()”.
"""



# Niveau 1
print("Bienvenue dans l'aventure !")
print("Vous êtes au niveau 1.")
print("Vous vous trouvez devant trois portes :")
print("1. La porte rouge")
print("2. La porte bleue")
print("3. La porte verte")

# Demander au joueur de choisir une porte
choix_porte = input("Choisissez une porte (1/2/3) : ")

# Niveau 2
if choix_porte == "1":
    print("Vous entrez dans la pièce derrière la porte rouge.")
    print("Vous voyez un coffre verrouillé.")
    choix_coffre = input("Voulez-vous ouvrir le coffre (oui/non) ? ")
    if choix_coffre.lower() == "oui":
        print("Le coffre s'ouvre et vous trouvez une clé en or.")
        print("Vous pouvez maintenant ouvrir la porte bleue.")
        choix_porte = input("Choisissez une autre porte (2/3) : ")
        if choix_porte == "2":
            print("Vous entrez dans la pièce derrière la porte bleue.")
            print("Vous trouvez un miroir magique.")
            print("En regardant dans le miroir, vous obtenez la grande réponse sur la vie, l'univers et le reste !")
        else:
            print("Vous entrez dans la pièce derrière la porte verte.")
            print("Vous trouvez un trésor caché.")
            print("Félicitations ! Vous avez réussi l'aventure.")
    else:
        print("Vous décidez de ne pas ouvrir le coffre.")
        print("Vous choisissez une autre porte.")
        choix_porte = input("Choisissez une autre porte (2/3) : ")
        if choix_porte == "2":
            print("Vous entrez dans la pièce derrière la porte bleue.")
            print("Vous trouvez un miroir magique.")
            print("En regardant dans le miroir, vous obtenez la grande réponse sur la vie, l'univers et le reste !")
        else:
            print("Vous entrez dans la pièce derrière la porte verte.")
            print("Vous trouvez un trésor caché.")
            print("Félicitations ! Vous avez réussi l'aventure.")
elif choix_porte == "2":
    print("Vous entrez dans la pièce derrière la porte bleue.")
    print("Vous trouvez un miroir magique.")
    print("En regardant dans le miroir, vous obtenez la grande réponse sur la vie, l'univers et le reste !")
else:
    print("Vous entrez dans la pièce derrière la porte verte.")
    print("Vous trouvez un trésor caché.")
    print("Félicitations ! Vous avez réussi l'aventure.")



