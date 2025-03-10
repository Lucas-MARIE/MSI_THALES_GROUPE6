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
            model="llama3-8b-8192",
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

                consigne = "Renvoie uniquement ceci."

                # Prompt Groq
                factor_dev = "En français, renvoie une liste de facteur de développement étudié dans l'étude ayant pour url "+url+"."+consigne +"Prends cet exemple comme modèle pour générer ta réponse : Selon l'étude disponible à l'URL https://www.semanticscholar.org/paper/1a6f7830c631b57dcdd0154b4dd166d47205b6f1, les facteurs de développement étudiés incluent le coefficient de Gini, l'Indice de Développement Humain (IDH), le revenu national brut (RNB) par habitant, l'espérance de vie à la naissance, les années d'école attendues, les années d'école moyennes, le taux de croissance de la population, le taux de mortalité infantile, le taux de mortalité sous-5 ans, le ratio de mortalité maternelle, le taux de fecondité totale, la prévalence des méthodes contraceptives, l'accès aux sources d'eau améliorées, l'accès aux installations sanitaires améliorées, l'accès à l'électricité, l'accès à internet, la pénétration des téléphones portables, le soutien social, la liberté de prendre des choix de vie, la générosité et les normes sociales."
                factor_precisions = "En français, décrit ici les effets étudiés dans l'étude ayant pour url "+url+"."+consigne + "Prends cet exemple comme modèle pour générer ta réponse : L'étude examine les effets de différents facteurs de développement sur la santé et le bien-être des populations. Elle étudie les liens entre ces facteurs et les indicateurs de santé tels que la mortalité infantile, la mortalité sous-5 ans, la mortalité maternelle, la prévalence des maladies chroniques et la qualité de vie. Les effets étudiés incluent également les impacts sur la pauvreté, la pauvreté infantile, la scolarisation, la santé mentale et le bien-être subjectif."
                country = "En français, indique ici les différents pays dans lequel ou lesquels l'étude ayant pour url "+url+" porte."+consigne + "Prends cet exemple comme modèle pour générer ta réponse : L'étude examine les données de 146 pays, notamment les pays suivants : Afrique du Sud, Algérie, Angola, Argentine, Arménie, Australie, Autriche, Bangladesh, Belgique, Bolivie, Brésil, Bulgarie, Canada, Chili, Chine, Colombie, Costa Rica, Côte d'Ivoire, Croatie, Danemark, Égypte, Équateur, Espagne, États-Unis, Fidji, Finlande, France, Gabon, Géorgie, Ghana, Grèce, Guatemala, Honduras, Hongrie, Inde, Indonésie, Irak, Iran, Irlande, Israël, Italie, Japon, Jordanie, Kazakhstan, Kenya, Kirghizistan, Koweït, Lettonie, Liban, Lituanie, Luxembourg, Macédoine, Malaisie, Malawi, Mali, Maroc, Mexique, Moldavie, Mongolie, Monténégro, Mozambique, Namibie, Népal, Nicaragua, Nigéria, Norvège, Nouvelle-Zélande, Oman, Ouganda, Pakistan, Pologne, Portugal, Qatar, République centrafricaine, République démocratique du Congo, République dominicaine, Roumanie, Russie, Rwanda, Saint-Marin, Salvador, Sénégal, Serbie, Sierra Leone, Singapour, Slovaquie, Slovénie, Somalie, Soudan, Soudan du Sud, Sri Lanka, Suède, Suisse, Syrie, Tadjikistan, Tanzanie, Thaïlande, Togo, Tunisie, Turquie, Ukraine, Uruguay, Venezuela, Viêt Nam, Yémen, Zambie et Zimbabwe."
                data_s = "En français, indique ici les différentes sources de la ou lesquelle(s) l'étude ayant pour url "+url+" porte."+consigne + "Prends cet exemple comme modèle pour générer ta réponse : L'étude utilise les données suivantes comme sources : World Development Indicators (WDI), World Health Organization (WHO), United Nations Children's Fund (UNICEF), World Bank, Human Development Report (HDR), Global Health Observatory (GHO), Demographic and Health Surveys (DHS), Multiple Indicator Cluster Surveys (MICS), and the World Values Survey (WVS)."
                year_s = "En français, indique ici l'année des données utilisées des sources de la ou lesquelle(s) l'étude ayant pour url "+url+" porte."+consigne + "Prends cet exemple comme modèle pour générer ta réponse : Les données utilisées dans l'étude datent de 2015."
                methode = "En français, indique ici la méthodologie utilisé pour les différents facteurs de l'étude ayant pour url "+url+"."+consigne + "Prends cet exemple comme modèle pour générer ta réponse : La méthodologie utilisée dans l'étude consiste en une analyse de corrélations entre les facteurs de développement et les indicateurs de santé, utilisant des modèles de régression linéaire et des analyses de variance. Les données sont collectées à partir de sources secondaires et sont traitées à l'aide de logiciels de traitement de données."

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



                file_content += f'{url};{publicationTypes};{publicationDate};{title};{t_rep[0]};{t_rep[1]};{t_rep[2]};{t_rep[3]};{t_rep[4]};{t_rep[5]};{abstract}\n'
                count+=1

            file.write(file_content)
            print(f"Les données ont été exportées avec succès dans '{csv_file}'.")
        else:
            print("Le fichier JSON ne contient pas une liste.")
