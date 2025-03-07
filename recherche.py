import requests
import json

def research(query0,query1,query2,query3, query4, query5, query6, query7, query8, query9, query10,nombreReponse,affiche):
    
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
        listeReponse = []

        # Si aucun document n'est trouvé, affiche un message
        if reponse['total'] == 0:
            print("Aucun document trouvé, essayez une requête moins spécifique","\n")
        
        else:
            # écrit les résultats dans une liste
            with open(f"articles.json", "a") as file:
                if nombreReponse<reponse['total']:
                    print("Nous avons trouvé ",reponse['total'], "résultats","\n")
                    for i in range (nombreReponse) :
                        listeReponse.append(reponse["data"][i])           
                    for i in range (affiche) :
                        print(reponse["data"][i], "\n")
                        print(f"les {nombreReponse} articles ont bien été enregistrés dans le fichier articles.json","\n")
                        print("-------------------------------------------","\n")
                #exeption si le nombre de réponse est supérieur au nombre de résultats
                else:
                    print("Nous avons trouvé ",reponse['total'], "résultats","\n")
                    for i in range (reponse['total']) :
                        listeReponse.append(reponse["data"][i])            
                    if reponse['total']>0:
                        for i in range (affiche) :
                            print(reponse["data"][i], "\n")
                            print(f"les {reponse['total']} articles ont bien été enregistrés dans le fichier articles.json","\n")
                            print("-------------------------------------------","\n")

        # écrit la listeResultat dans un fichier json sans ecraser le contenue précédent, utile en cas d'erreurs   
        with open('articles.json', 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
            data.append(listeReponse)
        with open('articles.json', 'w') as file:
            json.dump(data, file)
