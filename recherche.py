import requests
import json

# Specifie les parametres de la requête 
# une première requète générale puis une par facteur de développement
# partie à optimiser pour la suite
query0 = 'Digital identity system and developing countries'
query1 = 'Digital identity system and financial inclusion'
query2 = 'Digital identity system and Property rights'
query3 = 'Digital identity system and health'
query4 = 'Digital identity system and vaccination'
query5 = 'Digital identity system and education'
query6 = 'Digital identity system and age'
query7 = 'Digital identity system and corruption'
query8 = 'Digital identity system and salary declaration'
query9 = 'Digital identity system and taxes'
query10 = 'Digital identity system and work access'
# Nombre de réponses souhaitées par requête
nombreReponse = 10
affiche = 1


# défini l'URL de l'API
#/paper/search trie les documents par "relevance" par rapport aux mots clés de la requête
url = "https://api.semanticscholar.org/graph/v1/paper/search"


# Défini les paramètres de la requête pour chaque boucle
for query in [query0, query1, query2, query3, query4, query5, query6, query7, query8, query9, query10]:
    query_params = {
        "query": query,
        #quelles informations veut-on récupérer?
        "fields": "title,url,publicationTypes,citationCount,publicationDate,openAccessPdf,abstract,authors,references",
        "year": "2000-" ,
        #"minCitationCount": 10,
        "limit": nombreReponse , }

    # Envoie la requête et récupère les résultats
    reponse = requests.get(url, params=query_params).json()


    # Si aucun document n'est trouvé, affiche un message
    if reponse['total'] == 0:
        print("Aucun document trouvé, essayez une requête moins spécifique","\n")
    
    else:
        # écrit les résultats dans un fichier JSON
        with open(f"articles.json", "a") as file:
            if nombreReponse<reponse['total']:
                print("Nous avons trouvé ",reponse['total'], "résultats","\n")
                for i in range (nombreReponse) :
                    json.dump(reponse["data"][i], file, indent=4)            
                for i in range (affiche) :
                    print(reponse["data"][i], "\n")
                    print(f"les {nombreReponse} articles ont bien été enregistrés dans le fichier articles.json","\n")
                    print("-------------------------------------------","\n")
            #exeption si le nombre de réponse est supérieur au nombre de résultats
            else:
                print("Nous avons trouvé ",reponse['total'], "résultats","\n")
                for i in range (reponse['total']) :
                    json.dump(reponse["data"][i], file, indent=4)            
                if reponse['total']>0:
                    for i in range (affiche) :
                        print(reponse["data"][i], "\n")
                        print(f"les {reponse['total']} articles ont bien été enregistrés dans le fichier articles.json","\n")
                        print("-------------------------------------------","\n")
