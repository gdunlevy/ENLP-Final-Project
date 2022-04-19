import os , string
import pandas as pd
import spacy
from PyDictionary import PyDictionary
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.models import KeyedVectors,Word2Vec
from sklearn.metrics.pairwise import cosine_similarity


sp = spacy.load('en_core_web_sm')
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer() 



def read(f): 
	df = pd.read_csv(f)

	sentence = df.iloc[:, 1].tolist()
	for i in range(len(sentence)): 
		sentence[i] = sentence[i].lower()



	sentence = " ".join(sentence)


	stop_free = " ".join([i for i in sentence.lower().split() if i not in stop])

	# remove any stop words present
	punc_free = ''.join(ch for ch in stop_free if ch not in exclude)  

	# remove punctuations + normalize the text
	normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split()) 
	print(normalized)

	return (normalized)

def pos(sentence): 

	dictionary=PyDictionary()
	sen = sp(sentence)

	sub_toks = [tok for tok in sen if (tok.dep_ == "nsubj") ]

	sen2 = sp(str(sub_toks[0]))
	print(sen2)


	for i in sen:
		print("Similarity:", sen2.similarity(i))
		
	'''
	'I used to be a banker but I lost interest --> used banker lost interest 
		banker is the subject 
	check similarity of other words against the subject
		highest similarity is INTEREST (0.41) 
		
	
	'When the church nought gas for the barbecue, proceeds went from sacred to the propane. --> church bought gas annual barbecue proceeds went sacred propan
		church is the subject 
	check similarity of other words against the subject
		highest similarity is PROPANE (0.41) 
		
		
	I am not sure what to do about the puns with quotes.... 
	'''


def main():
    # parse xml file
    directory = 'semeval2017_task7/data/trial'

    for filename in os.listdir(directory):
	    f = os.path.join(directory, filename)
	    if os.path.isfile(f):
	    	if f.endswith((".csv")):
	    		#name = os.path.splitext(filename)[0]
	    		print(f)
	    		sentence = read(f)
	    		pos(sentence)

	    		#exit()




      
if __name__ == "__main__":
  
    # calling main function
    main()
