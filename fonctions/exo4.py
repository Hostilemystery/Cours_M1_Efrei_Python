"""  
 Faite en sorte de créer une fonction “tableGenerator” capable de générer un tableau
 matriciel avec des “|” et des ”-” d’après une liste python à plusieurs dimensions.
 Se tableau devra obligatoirement comprendre des titres pour chaque colonnes même
 vide et des valeurs même si vide.
 Appuyez-vous sur la structure de votre liste pour reproduire votre tableau à l’identique
 dans votre console.
"""


def tableGenerator(donnee, titre):
    largeur_colone = [max(len(str(item)) for item in col) for col in zip(*donnee, titre)]
    
    ligne_horizontal = '+' + '+'.join('-' * (largeur + 2) for largeur in largeur_colone) + '+'
    
    # Create the header row
    titre_ligne = '| ' + ' | '.join(f'{titre:<{largeur_colone[i]}}' for i, titre in enumerate(titre)) + ' |'
    
    
    donee_ligne = []
    for row in donnee:
        donee_ligne.append('| ' + ' | '.join(f'{item:<{largeur_colone[i]}}' for i, item in enumerate(row)) + ' |')
    
    
    table = [ligne_horizontal, titre_ligne, ligne_horizontal] + donee_ligne + [ligne_horizontal]
    return '\n'.join(table)

# Example data and headers
titre = ["", "Test1", "Test2", "Test3"]
donnee = [
    ["Data1", "1", "2", "3.33"],
    ["Data2", "3", "2", "1"],
    ["Data3", "6.7", "4", "2"]
]

# Generate and print the table
table = tableGenerator(donnee, titre)
print(table)
