from extracteur import *
from recherche import *

# Specifie les parametres de la requête 
# une première requète générale puis une par facteur de développement
# partie à optimiser pour la suite
query0 = 'identification system and developing countries'
query1 = 'birth registration and developing countries and health care'
query2 = 'birth registration and rights'
query3 = 'identification system and health care'
query4 = 'birth registration and vaccination'
query5 = 'birth registration and education'
query6 = 'identification system and corruption'
query7 = 'birth registration and corruption'
query8 = 'birth registration and salary declaration'
query9 = 'identification system and taxes'
query10 = 'birth registration and work access'
# Nombre de réponses souhaitées par requête
nombreReponse = 10
affiche = 1

research(query0,query1,query2,query3, query4, query5, query6, query7, query8, query9, query10,nombreReponse,affiche)

#spécifie les chemins d'accès
chemin_file= 'articles.json'
csv_file = 'resultats_export.csv'
chemin_acces = ""

extract(chemin_file,csv_file,chemin_acces)
