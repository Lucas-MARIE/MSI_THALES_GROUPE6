from groq import Groq
import json
import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

client = Groq(
    api_key=os.getenv("API_KEY"),
)

def chat_with_groq(l_prompt):
    response = {}
    try:
        for texte in l_prompt :
            response[texte]=[]
            r = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Sans sauter de ligne et sans utiliser de retour à la ligne, répond à cette requête:"+texte,
                }
            ],
            temperature=0.2,
            model="llama3-70b-8192",
            )
            response[texte].append(r.choices[0].message.content)
        # Extraire et retourner la réponse du modèle
        return response

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None

def extract(chemin_file,csv_file,chemin_acces):

    # On ouvre le fichier JSON
    with open(chemin_file, 'r') as file:
        data = json.load(file)  # Charger le fichier JSON sous forme de liste de dictionnaires

    # On ouvre le fichier CSV dans le but d'écrire les données des articles
    with open(chemin_acces+csv_file, mode='w', encoding='utf-8') as file:
        # On commence par écrire l'entête
        file.write('URL;PublicationTypes;publicationDate;Title;Facteurs_dev;Facteurs_precisions;Pays;Date_source;Année_source;Méthode;Abstract\n')
        file_content = ""

        # On vérifie que le JSON est bien sous forme de liste
        if isinstance(data, list):
            # On récupère les données de chacun des articles récoltés
            count = 1
            for item in data:
                print("Data n°"+str(count)+"/"+str(len(data)))

                # On extrait les données qui nous interessent
                url = item.get('url', '')
                title = item.get('title', '')
                abstract = item.get('abstract', '')
                citationCount = item.get('citationCount', '')
                publicationTypes = item.get('publicationTypes', '')
                publicationDate = item.get('publicationDate', '')
                authors = item.get('authors','')

                # Prompt Groq
                factor_dev = "En français, renvoie une liste de facteur de développement étudié dans l'étude ayant pour url "+url+". Renvoie uniquement ceci."
                factor_precisions = "En français, décrit ici les effets étudiés dans l'étude ayant pour url "+url+". Renvoie uniquement ceci."
                country = "En français, indique ici les différents pays dans lequel ou lesquels l'étude ayant pour url "+url+" porte. Renvoie uniquement ceci."
                data_s = "En français, indique ici les différentes sources de la ou lesquelle(s) l'étude ayant pour url "+url+" porte. Renvoie uniquement ceci."
                year_s = "En français, indique ici l'année des données utilisées des sources de la ou lesquelle(s) l'étude ayant pour url "+url+" porte. Renvoie uniquement ceci."
                methode = "En français, indique ici la méthodologie utilisé pour les différents facteurs de l'étude ayant pour url "+url+". Renvoie uniquement ceci."

                t_rep=[factor_dev,factor_precisions,country,data_s,year_s,methode]
                requ = chat_with_groq(t_rep)

                i=0
                first=True
                for el in requ:
                    for rows in requ[el]:
                        if first :
                            t_rep[i]=rows
                            first=False
                        else :
                            t_rep[i]+=rows
                    i+=1
                    first=True



                file_content = f'{url};{publicationTypes};{publicationDate};{title};{t_rep[0]};{t_rep[1]};{t_rep[2]};{t_rep[3]};{t_rep[4]};{t_rep[5]};{abstract}\n'
                count+=1

                file.write(file_content)
                print(f"Les données ont été exportées avec succès dans '{csv_file}'.")
            else:
                print("Le fichier JSON ne contient pas une liste.")

            
