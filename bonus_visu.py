# Créer un diagramme en bâtons pour les facteurs de développement
#pour chaque valeur dans la colonne si la valeur contient un des facteurs de développement de la liste fact_dev alors la valeur de la colonne facteur devient égale à ce facteur

fact_dev = ["Accès aux services financiers","Accès aux soins", "Droits à la propriété", 'Accès à la vaccinatio' , 'Accès à l’éducation et à la diplomation'  , 'Justification de l’âge'  , 'Élimination de la corruption'  , 'Les salaires et travailleurs fantômes'  , 'L’enregistrement pour les impôts' , 'Accès au travail']

def facteur_dev(data):
    for i in range(len(data['Facteurs_dev'])):
        for facteur in fact_dev:
            if facteur in data['Facteurs_dev'][i]:
                return facteur
        print(data['Facteurs_dev'][i])    
        return  'Autre'

data['Facteurs_dev'] = data.apply(facteur_dev, axis=1)

        

# Compter les occurrences de chaque facteur de développement
factor_counts = data['Facteurs_dev'].value_counts()

    
# Créer un diagramme en bâtons pour les facteurs de développement
plt.figure(figsize=(12, 8))
factor_counts.plot(kind='bar')
plt.title('Occurrences des différents facteurs de développement')
plt.xlabel('Facteurs de développement')
plt.ylabel('Nombre d\'occurrences')
plt.xticks(rotation=45, ha='right')

# Afficher le diagramme en bâtons pour les facteurs de développement
plt.tight_layout()
plt.show()
