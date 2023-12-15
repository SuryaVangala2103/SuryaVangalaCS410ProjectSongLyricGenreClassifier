import pickle
from os import listdir
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier

nltk.download("wordnet")
hip_hop = "Song_Lyric_Data/Hip_Hop"
pop = "Song_Lyric_Data/Pop"
country = "Song_Lyric_Data/Country"
rock = "Song_Lyric_Data/Rock"
categories = [hip_hop, pop, country, rock]
category_labels = ["Hip_Hop", "Pop", "Country", "Rock"]
corpus = []
labels = []
lemmatizer = WordNetLemmatizer()
for i in range(len(categories)):
    files = [file for file in listdir(categories[i])]
    for f in files:
        filepath = categories[i] + "/" + f
        file = open(filepath, "r")
        lyrics = file.read().lower().replace("\n", "").split()
        lyrics = [word for word in lyrics if word not in stopwords.words('english')]
        lyrics = [lemmatizer.lemmatize(word) for word in lyrics]
        lyrics = "".join(lyrics)
        corpus.append(lyrics)
        labels.append(category_labels[i])

train_corpus, test_corpus, train_labels, test_labels = train_test_split(corpus, labels, test_size=0.2, random_state=42)
v = TfidfVectorizer()
train_corpus_v = v.fit_transform(train_corpus)
test_corpus_v = v.transform(test_corpus)
classifier = DecisionTreeClassifier(max_depth=3, random_state=42)
model = classifier.fit(train_corpus_v, train_labels)
score = model.score(test_corpus_v, test_labels)
file = open("Model_Test_Score.txt", "w")
file.write(str(score))
file.close()
pickle.dump(model, open('model.pkl','wb'))
pickle.dump(v, open('vectorizer.pkl', 'wb'))

def prepare_input(song_lyrics, vectorizer):
    input_lemmatizer = WordNetLemmatizer()
    song_lyrics = song_lyrics.lower().replace("\n", "").split()
    song_lyrics = [word for word in song_lyrics if word not in stopwords.words('english')]
    song_lyrics = [input_lemmatizer.lemmatize(word) for word in song_lyrics]
    song_lyrics = "".join(song_lyrics)
    lyrics_list = [song_lyrics]
    output = v.transform(lyrics_list)
    return output
