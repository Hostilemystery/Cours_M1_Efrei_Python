"""  
 Faite en sorte de créer une fonction “tableGenerator” capable de générer un tableau
 matriciel avec des “|” et des ”-” d’après une liste python à plusieurs dimensions.
 Se tableau devra obligatoirement comprendre des titres pour chaque colonnes même
 vide et des valeurs même si vide.
 Appuyez-vous sur la structure de votre liste pour reproduire votre tableau à l’identique
 dans votre console.
"""

table = [
    ["", "Test1", "Test2", "Test3"],
    ["Data1", "1", "2", "3.33"],
    ["Data2","3", "2", "1"],
    ["Data3","6.7", "4", "2"]
]

def get_biggest_chars(table):
    headers = [""]*len(table[0])
    for row in table:
        for i, element in enumerate(row):
            if len(str(element)) > len(headers[i]):
                headers[i] = element
    return headers

# print(get_biggest_chars(table))

def tableGenerator(table):
    biggestWordsByCol = get_biggest_chars(table)
    separator = f'|{'|'.join(list(map(lambda x: len(x) * '-', biggestWordsByCol)))}'
    for i, row in enumerate(table):
        rowStr = ""
        
        for j, col in enumerate(row):
          spaces = (len(biggestWordsByCol[i]) - len(col)) * ' '
          rowStr += f'|{col}{spaces}'
        
        if(not i) :
           rowStr += f'|\n{separator}'
        print(f'{rowStr}|')



tableGenerator(table)