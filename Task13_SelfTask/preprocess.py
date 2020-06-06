import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

lemmatizer = WordNetLemmatizer()

stopwords = nltk.corpus.stopwords.words('english')
stemmer = PorterStemmer()

#Defining pre-process function
def pre_process(doc):
    text=nltk.sent_tokenize(doc)
    tokens = [[word for word in nltk.word_tokenize(sent)] for sent in text ]
    tokens= [[w for w in sent if w not in stopwords] for sent in tokens]
    tokens = [[w.lower() for w in sent if w.isalpha()] for sent in tokens ]
    #stems = [[stemmer.stem(t) for t in sent] for sent in tokens]
    lemma = [[lemmatizer.lemmatize(t) for t in sent] for sent in tokens]
    return lemma

if __name__ == "__main__":
    
    path = input('Please Enter Directory Path: ')
    print ('Reading files...')
    file = path+".txt"
    docs=open(file,'r',errors='ignore').read()
    
    #preprocessing files
    print ("Preprocessing data extracted...")
    texts=pre_process(docs)
    print (texts)
 
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(nltk.sent_tokenize(docs))
    print(vectorizer.get_feature_names())
    print(X.toarray())