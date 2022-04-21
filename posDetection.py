import os , string
import pandas as pd
import spacy
from PyDictionary import PyDictionary
from pprint import pprint
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
from gensim.models import KeyedVectors,Word2Vec
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import wordnet as wn


sp = spacy.load('en_core_web_sm')
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer() 



def read(f): 
	df = pd.read_csv(f)
	
	for index, row in df.iterrows():
		full_sentence = row['Sentence']


		stop_free = " ".join([i for i in full_sentence.lower().split() if i not in stop])

		# remove any stop words present
		punc_free = ''.join(ch for ch in stop_free if ch not in exclude)  

		# remove punctuations + normalize the text
		#normalized = " ".join(lemma.lemmatize(word,'v') for word in punc_free.split())
		normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split()) 

		#return (normalized)


		return full_sentence

def pos(sentence): 

	dictionary=PyDictionary()
	sen = sp(sentence)

	'''
	sub_toks = [tok for tok in sen if (tok.dep_ == "nsubj") ]
	sen2 = sp(str(sub_toks[0]))

	for i in sen:
		print(i)
		for j in sen: 
			print('Similarity with ',i,' and ',j, ': ',i.path_similarity(j))
			#print('Similarity with ',i,' and ',j, ': ',i.similarity(j))
			#print("Similarity:", sen2.similarity(i))

	

	'''

	print(sentence)
	for i in range(len(sentence)):
		print(sentence[i])
		pprint(wn.synsets(sentence[i])) 
	exit()
	'''
	for word in sen:
		print(word)

		print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
		print(word.pos_)

		
			#wn.synsets(str(word), word.tag_)
		#if word.pos_ == 'DET' or word.pos_ == 'CCONJ' or word.pos_ == 'PUNCT' or word.pos_ =='PART': 
		#definition = dictionary.meaning(str(word))
		#print(definition)
	'''

	'''
	can split up definitions based off of the PoS tag given 
	some will have to be based off the tags (when it is an AUX)
		VB --> verb 
	can ignore DET and CCONJ and PUNCT


	check for multiple definitions of 

	
	'''
def main():
    # parse xml file
    directory = 'semeval2017_task7/data/trial'

    for filename in os.listdir(directory):
	    f = os.path.join(directory, filename)
	    if os.path.isfile(f):
	    	if f.endswith(("puns.csv")):
	    		#name = os.path.splitext(filename)[0]
	    		print(f)
	    		sentence = read(f)
	    		pos(sentence)

	    		#exit()




      
if __name__ == "__main__":
  
    # calling main function
    main()
