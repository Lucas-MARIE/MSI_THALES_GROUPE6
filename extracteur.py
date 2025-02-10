import openai
import json


openai.api_key = 'nom de clé'

def chat_with_gpt(prompt):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Ou "gpt-4" selon le modèle que tu utilises
            prompt=prompt,
            max_tokens=150,  # Le nombre maximum de tokens dans la réponse
            n=1,  # Nombre de réponses générées
            stop=None,  # Tu peux définir un critère d'arrêt si besoin
            temperature=0.7  # Plus la température est élevée, plus la réponse est créative
        )
        
        # Extraire et retourner la réponse du modèle
        return response.choices[0].text.strip()

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None

# On ouvre le fichier JSON
with open('articles.json', 'r') as file:
    data = json.load(file)  # Charger le fichier JSON sous forme de liste de dictionnaires

# On crée le fichicher CSV
csv_file = 'resultats_export.csv'

# On ouvre le fichier CSV dans le but d'écrire les données des articles
with open(csv_file, mode='w', encoding='utf-8') as file:
    # On commence par écrire l'entête
    file.write('URL;PublicationTypes;publicationDate;Title;Abstract\n')

    # On vérifie que le JSON est bien sous forme de liste
    if isinstance(data, list):
        # On récupère les données de chacun des articles récoltés
        for item in data:
            # On extrait les données qui nous interessent
            url = item.get('url', '')
            title = item.get('title', '')
            abstract = item.get('abstract', '')
            citationCount = item.get('citationCount', '')
            publicationTypes = item.get('publicationTypes', '')
            publicationDate = item.get('publicationDate', '')
            authors = item.get('authors','')

            # Prompt Chat GPT
            factor_dev = "En français, renvoie une liste de facteur de développement étudié dans l'étude ayant pour url "+url+". Renvoie uniquement ceci."
            factor_precisions = "En français, décrit ici les effets étudiés dans l'étude ayant pour url "+url+". Renvoie uniquement ceci."
            country = "En français, indique ici les différents pays dans lequel ou lesquels l'étude ayant pour url "+url+" porte. Renvoie uniquement ceci."
            data_s = "En français, indique ici les différentes sources de la ou lesquelle(s) l'étude ayant pour url "+url+" porte. Renvoie uniquement ceci."
            year_s = "En français, indique ici l'année des données utilisées des sources de la ou lesquelle(s) l'étude ayant pour url "+url+" porte. Renvoie uniquement ceci."
            methode = "En français, indique ici la méthodologie utilisé pour les différents facteurs de l'étude ayant pour url "+url+". Renvoie uniquement ceci."

            # L'interrogatoire ...
            #factor_dev = chat_with_gpt(factor_dev)
            #factor_precisions = chat_with_gpt(factor_precisions)
            #country = chat_with_gpt(country)
            #data_s = chat_with_gpt(data_s)
            #year_s = chat_with_gpt(year_s)
            #methode = chat_with_gpt(methode)

            # On stock les données dans une variable

            #if not(factor_dev) or not(factor_precisions) or not(country) or not(data_s) or not(year_s) or not(methode):
                #print("Problème avec l'un des prompts.")
            #else :
            line = f'{url};{publicationTypes};{publicationDate};{title};{abstract}\n'
            # On écrit la ligne dans le fichier CSV
            file.write(line)

        print(f"Les données ont été exportées avec succès dans '{csv_file}'.")
    else:
        print("Le fichier JSON ne contient pas une liste.")
