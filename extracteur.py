from dotenv import load_dotenv
from groq import Groq
import json
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

client = Groq(
    api_key=os.getenv("API_KEY"),
)

def chat_with_groq(prompt):
    try:
        r = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Sans sauter de ligne et sans utiliser de retour à la ligne, répond à cette requête:"+prompt,
            }
        ],
        temperature=0.2,
        model="llama3-70b-8192",
        )
        # Extraire et retourner la réponse du modèle
        return r.choices[0].message.content

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
        file.write('Titre;URL;publicationDate;Facteurs_dev;Facteurs_precisions;Pays;PublicationTypes;Date_source;Année_source;Méthode\n')
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
                publicationTypes = item.get('publicationTypes', '')
                abstract = str(item.get('abstract', ''))
                publicationDate = item.get('publicationDate', '')
                
                #authors = item.get('authors','')
                #citationCount = item.get('citationCount', '')

                # Prompt Groq
                factor_dev = "En français, renvoie une liste de facteur de développement étudié dans l'étude ayant pour titre  "+title+" et pour abstract" + abstract +". Renvoie uniquement ceci. Exemple de réponse : Accès à l'éducation et à la diplomation."
                factor_precisions = "En français, décrit ici les effets étudiés dans l'étude ayant pour titre  "+title+" et pour abstract" + abstract +". Renvoie uniquement ceci. Exemple de réponse : Effet de l'absence de certificat de naissance sur la progression scolaire et la diplomation primaire. "
                country = "En français, indique ici les différents pays dans lequel ou lesquels l'étude ayant pour titre  "+title+" et pour abstract" + abstract +". Renvoie uniquement ceci. Exemple de réponse : République Dominicaine"
                data_s = "En français, indique ici les différentes sources de la ou lesquelle(s) l'étude ayant pour titre  "+title+" et pour abstract" + abstract +". Renvoie uniquement ceci. Exemple de réponse : UNICEF, UNESCO, DHS"
                year_s = "En français, indique ici l'année des données utilisées des sources de la ou lesquelle(s) l'étude ayant pour titre  "+title+" et pour abstract" + abstract +". Renvoie uniquement ceci. Exemple de réponse : 2007 pour DHS"
                methode = "En français, indique ici la méthodologie utilisé pour les différents facteurs de l'étude ayant pour titre  "+title+" et pour abstract" + abstract +". Renvoie uniquement ceci. Ne saute aucune ligne et ne dépasse pas le nombre de caractère maximum dans ta réponse : 10000. Exemple de réponse (en anglais, mais tu dois répondre en Français): GPS data: geographic location of civil registry offices for spatial analysis. Data limitation: no birth registration data for individuals >18. analysis excludes post-high-school education. Measure of distance to civil registry office, mother’s legal documentation status. Restriction to urban areas to reduce correlation with unobservable factors. Econometric validity tests performed to ensure reliability. Subgroup Analysis: Subgroups: gender, mother’s education, household income. Robustness Checks: Sensitivity analyses, alternative model specifications to test robustness."

                factor_dev = chat_with_groq(factor_dev)
                factor_precisions = chat_with_groq(factor_precisions)
                country = chat_with_groq(country)
                data_s = chat_with_groq(data_s)
                year_s = chat_with_groq(year_s)
                methode = chat_with_groq(methode)

                file_content = f'{title};{url};{publicationDate};{factor_dev};{factor_precisions};{country};{publicationTypes};{data_s};{year_s};{methode}\n'
                count+=1

                file.write(file_content)
                print(f"Les données ont été exportées avec succès dans '{csv_file}'.")
        else:
            print("Le fichier JSON ne contient pas une liste.")
