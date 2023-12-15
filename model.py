import pickle
from os import listdir
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier

#wordnet is needed for lemmatizer
nltk.download("wordnet")
#save song directories
hip_hop = "Song_Lyric_Data/Hip_Hop"
pop = "Song_Lyric_Data/Pop"
country = "Song_Lyric_Data/Country"
rock = "Song_Lyric_Data/Rock"
#save categories and labels
categories = [hip_hop, pop, country, rock]
category_labels = ["Hip_Hop", "Pop", "Country", "Rock"]
#initialize resulting lists
corpus = []
labels = []
#initialize lemmatizer
lemmatizer = WordNetLemmatizer()
for i in range(len(categories)):
    #obtain list of all files in each genre directory
    files = [file for file in listdir(categories[i])]
    for f in files:
        #open each file
        filepath = categories[i] + "/" + f
        file = open(filepath, "r")
        #read all text in file, convert to lowercase, remove newlines, and convert to list of words
        lyrics = file.read().lower().replace("\n", "").split()
        #remove stopwords
        lyrics = [word for word in lyrics if word not in stopwords.words('english')]
        #lemmatize remaining words
        lyrics = [lemmatizer.lemmatize(word) for word in lyrics]
        #join lyrics back into string
        lyrics = "".join(lyrics)
        #add lyrics to corpus and label to labels
        corpus.append(lyrics)
        labels.append(category_labels[i])

#train-test split 80-20
train_corpus, test_corpus, train_labels, test_labels = train_test_split(corpus, labels, test_size=0.2, random_state=42)
#initialize TF-IDF vectorization
v = TfidfVectorizer()
#TF-IDF on train and test
train_corpus_v = v.fit_transform(train_corpus)
test_corpus_v = v.transform(test_corpus)
#initialize classifier
classifier = DecisionTreeClassifier(max_depth=3, random_state=42)
#fit the model
model = classifier.fit(train_corpus_v, train_labels)
#score the model
score = model.score(test_corpus_v, test_labels)
#write model score to file
file = open("Model_Test_Score.txt", "w")
file.write(str(score))
file.close()
#pickle the model and the vectorizer for use in the app
pickle.dump(model, open('model.pkl','wb'))
pickle.dump(v, open('vectorizer.pkl', 'wb'))

#takes text input and turns it into data that the model can read
def prepare_input(song_lyrics, vectorizer):
    #initialize new lemmatizer
    input_lemmatizer = WordNetLemmatizer()
    #perform same steps as above to process text (stopwords, lowercase ect)
    song_lyrics = song_lyrics.lower().replace("\n", "").split()
    song_lyrics = [word for word in song_lyrics if word not in stopwords.words('english')]
    song_lyrics = [input_lemmatizer.lemmatize(word) for word in song_lyrics]
    song_lyrics = "".join(song_lyrics)
    lyrics_list = [song_lyrics]
    #transform input with same vectorizer as train and test data
    output = v.transform(lyrics_list)
    #return tensor
    return output
