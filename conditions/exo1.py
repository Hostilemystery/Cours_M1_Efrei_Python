""" 
Créer un script capable de faire entrer dans une boîte de nuit une personne ayant plus
de 18 ans et refusant celles qui ont entre 0 et 17 ans. Utilisez “print();” pour afficher
votre message. Vous devez faire une concaténation avec la phrase “Vous ne pouvez
pas entrer vous n’êtes pas majeur vous avez {age}” ou “Vous pouvez entrer vous
êtes majeur vous avez {age}”. Attention si l’âge est compris entre 42 et plus vous
devenez le patron de la boite !

"""

age = int(input("Entrer votre age : "))


print(f"Vous avez {age} ans et vous êtes le nouveau patron " if age >=42
      else f"Vous pouvez entrer vous êtes majeur vous avez {age} ans" if age > 17
      else f"Vous ne pouvez pas entrer vous n’êtes pas majeur vous avez {age} ans")

