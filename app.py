import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
from helper import clean_data,facteur_dev


# Charger les données
data = pd.read_csv(r"C:\Users\rayan\Downloads\resultats_export_lucas.csv", sep=';')

# Nettoyer les données pour les dates de publication
data['publicationDate'] = pd.to_datetime(data['publicationDate'], errors='coerce')
clean_data(data)

# Nuage de mots pour les titres
st.title("Nuage de mots des titres")
text = " ".join(titre for titre in data.Titre.dropna())
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
st.pyplot(plt)

# Graphique des dates de publications
st.title("Graphique des dates de publications")
data['year'] = data['publicationDate'].dt.year
plt.figure(figsize=(10,5))
sns.histplot(data['year'].dropna(), bins=30, kde=True)
plt.xlabel('Année de publication')
plt.ylabel('Nombre de publications')
plt.title('Distribution des dates de publications')
plt.show()
st.pyplot(plt)


st.title("Proportions des pays")
country_counts = data['Pays'].value_counts()
plt.figure(figsize=(10,5))
sns.barplot(x=country_counts.values, y=country_counts.index)
plt.xlabel('Nombre de publications')
plt.ylabel('Pays')
plt.title('Proportions des pays')
st.pyplot(plt)


# Créer un diagramme en bâtons pour les facteurs de développement
#pour chaque valeur dans la colonne si la valeur contient un des facteurs de développement de la liste fact_dev alors la valeur de la colonne facteur devient égale à ce facteur




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
st.pyplot(plt)