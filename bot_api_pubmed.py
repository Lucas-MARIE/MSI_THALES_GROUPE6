import requests
import json
import os
import xml.etree.ElementTree as ET

# Étape 1 : Rechercher des articles pertinents

# URL de base pour les requêtes de recherche
search_base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

# Paramètres de la requête de recherche
search_params = {
    'db': 'pubmed',  # Base de données à interroger
    'term': 'Digital identity systems AND financial inclusion',  # Termes de recherche
    'retmode': 'json',  # Format de la réponse
    'retmax': 20  # Nombre maximum de résultats à retourner
}

# Faire la requête de recherche
search_response = requests.get(search_base_url, params=search_params)

# Vérifier le statut de la réponse de recherche
if search_response.status_code == 200:
    try:
        search_results = search_response.json()
        print("Résultats de la recherche :", search_results)
    except json.JSONDecodeError:
        print("Erreur de décodage JSON pour la recherche :", search_response.text)
        exit()  # Arrêter le programme si la recherche échoue
else:
    print(f"Erreur lors de la recherche : {search_response.status_code}")
    print("Contenu de la réponse :", search_response.text)
    exit()  # Arrêter le programme si la recherche échoue

# Étape 2 : Récupérer les détails des articles

# URL de base pour les requêtes de récupération
fetch_base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Identifiants des articles à récupérer (à partir de la recherche précédente)
article_ids = search_results['esearchresult']['idlist']

# Paramètres de la requête de récupération
fetch_params = {
    'db': 'pubmed',  # Base de données à interroger
    'id': ','.join(article_ids),  # Identifiants des articles à récupérer
    'retmode': 'xml',  # Format de la réponse (XML dans ce cas)
    'rettype': 'abstract'  # Type de retour (résumé dans ce cas)
}

# Faire la requête de récupération
fetch_response = requests.get(fetch_base_url, params=fetch_params)

# Vérifier le statut de la réponse de récupération
if fetch_response.status_code == 200:
    try:
        articles_xml = fetch_response.text
        print("Détails des articles (XML) :", articles_xml)
    except Exception as e:
        print("Erreur lors de la récupération des articles :", e)
        exit()  # Arrêter le programme si la récupération échoue
else:
    print(f"Erreur lors de la récupération des articles : {fetch_response.status_code}")
    print("Contenu de la réponse :", fetch_response.text)
    exit()  # Arrêter le programme si la récupération échoue

# Étape 3 : Analyser et filtrer les articles

def parse_xml_to_json(xml_data):
    root = ET.fromstring(xml_data)
    articles = []
    for article in root.findall('.//PubmedArticle'):
        title = article.find('.//ArticleTitle').text
        abstract = article.find('.//AbstractText').text
        articles.append({'title': title, 'abstract': abstract})
    return articles

# Convertir les articles XML en JSON
articles = parse_xml_to_json(articles_xml)
print("Articles convertis en JSON :", articles)

# Étape 4 : Enregistrer les articles filtrés dans un fichier JSON sur le bureau

# Chemin vers le bureau
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
print("Chemin vers le bureau :", desktop_path)

# Nom du fichier JSON
file_name = 'filtered_articles.json'

# Chemin complet du fichier JSON
file_path = os.path.join(desktop_path, file_name)
print("Chemin complet du fichier JSON :", file_path)

# Enregistrer les articles filtrés dans un fichier JSON
with open(file_path, 'w') as f:
    json.dump(articles, f, indent=4)

print(f"Les articles filtrés ont été enregistrés dans '{file_path}'")
