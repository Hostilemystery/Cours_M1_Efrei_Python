""" 
Faire une liste partant de 1980 à nos jours en prenant en compte l’année actuelle
actualisé
"""

import datetime

year = datetime.date.today().year
liste_année =[]

for i in range(1980,year+1):
    liste_année.append(i)
    
print(liste_année)