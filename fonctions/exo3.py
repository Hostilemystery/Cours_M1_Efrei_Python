"""  
 Créer une fonction “detectMyAgeByNight” capable d’implémenter votre précédent
 script de la boîte de nuit et de faire entrer dans une boîte de nuit une personne ayant
 plus de 18 ans et refusant celles qui ont entre 0 et 17.
"""

def detectMyAgeByNight(age):
    if age < 18 : 
        return f"Vous ne pouvez pas entrez vous n’êtes pas majeur vous avez {age} ans"
    else:
        return f"Vous pouvez entrer vous êtes majeur vous avez {age} ans"

age = int(input("Entrer votre age : "))

print(detectMyAgeByNight(age))