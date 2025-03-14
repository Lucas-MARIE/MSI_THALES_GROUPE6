pays = [
    "Afghanistan", "Afrique du Sud", "Albanie", "Algérie", "Allemagne", "Andorre", "Angola",
    "Antigua-et-Barbuda", "Arabie saoudite", "Argentine", "Arménie", "Australie", "Autriche",
    "Azerbaïdjan", "Bahamas", "Bahreïn", "Bangladesh", "Barbade", "Belgique", "Belize", "Bénin",
    "Bhoutan", "Biélorussie", "Birmanie", "Bolivie", "Bosnie-Herzégovine", "Botswana", "Brésil",
    "Brunei", "Bulgarie", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodge", "Cameroun", "Canada",
    "Chili", "Chine", "Chypre", "Colombie", "Comores", "Congo", "Corée du Nord", "Corée du Sud",
    "Costa Rica", "Côte d'Ivoire", "Croatie", "Cuba", "Danemark", "Djibouti", "Dominique", "Égypte",
    "Émirats arabes unis", "Équateur", "Érythrée", "Espagne", "Estonie", "Eswatini", "États-Unis",
    "Éthiopie", "Fidji", "Finlande", "France", "Gabon", "Gambie", "Géorgie", "Ghana", "Grèce",
    "Grenade", "Guatemala", "Guinée", "Guinée-Bissau", "Guinée équatoriale", "Guyana", "Haïti",
    "Honduras", "Hongrie", "Îles Salomon", "Inde", "Indonésie", "Irak", "Iran", "Irlande", "Islande",
    "Israël", "Italie", "Jamaïque", "Japon", "Jordanie", "Kazakhstan", "Kenya", "Kirghizistan",
    "Kiribati", "Koweït", "Laos", "Lesotho", "Lettonie", "Liban", "Liberia", "Libye", "Liechtenstein",
    "Lituanie", "Luxembourg", "Macédoine du Nord", "Madagascar", "Malaisie", "Malawi", "Maldives",
    "Mali", "Malte", "Maroc", "Marshall", "Maurice", "Mauritanie", "Mexique", "Micronésie", "Moldavie",
    "Monaco", "Mongolie", "Monténégro", "Mozambique", "Namibie", "Nauru", "Népal", "Nicaragua",
    "Niger", "Nigéria", "Norvège", "Nouvelle-Zélande", "Oman", "Ouganda", "Ouzbékistan", "Pakistan",
    "Palaos", "Panama", "Papouasie-Nouvelle-Guinée", "Paraguay", "Pays-Bas", "Pérou", "Philippines",
    "Pologne", "Portugal", "Qatar", "République centrafricaine", "République dominicaine",
    "République tchèque", "Roumanie", "Royaume-Uni", "Russie", "Rwanda", "Saint-Kitts-et-Nevis",
    "Saint-Vincent-et-les-Grenadines", "Sainte-Lucie", "Saint-Marin", "Salvador", "Samoa", "São Tomé-et-Principe",
    "Sénégal", "Serbie", "Seychelles", "Sierra Leone", "Singapour", "Slovaquie", "Slovénie", "Somalie",
    "Soudan", "Soudan du Sud", "Sri Lanka", "Suède", "Suisse", "Suriname", "Syrie", "Tadjikistan",
    "Tanzanie", "Tchad", "Thaïlande", "Timor oriental", "Togo", "Tonga", "Trinité-et-Tobago", "Tunisie",
    "Turkménistan", "Turquie", "Tuvalu", "Ukraine", "Uruguay", "Vanuatu", "Vatican", "Venezuela",
    "Viêt Nam", "Yémen", "Zambie", "Zimbabwe"
]

def contient_pays(prompt):
    for i in pays:
        try:
            if i in prompt:
                return i
        except:
            return None
    return None




def clean_data(data):
    for i in range(len(data['Pays'])):
        data.at[i,'Pays'] = contient_pays(data['Pays'][i])



fact_dev = ["Accès aux services financiers","Accès aux soins", "Droits à la propriété", 'Accès à la vaccinatio' , 'Accès à l’éducation et à la diplomation'  , 'Justification de l’âge'  , 'Élimination de la corruption'  , 'Les salaires et travailleurs fantômes'  , 'L’enregistrement pour les impôts' , 'Accès au travail']
def facteur_dev(data):
        for facteur in fact_dev:
            if facteur in data['Facteurs_dev']:
                return facteur
        print(data['Facteurs_dev'])
        return  'Autre'