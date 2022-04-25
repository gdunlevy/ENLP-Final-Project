import pandas as pd
import os, ast, string
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


def pos_homographic(subtask1_homographic):
	print (subtask1_homographic)


	for i in subtask1_homographic: 
		if i.endswith("txt"): 
			print(i)
			#df = pd.read_csv(i)
			with open(i, 'r') as f:
				data = f.read()
				dictionary = ast.literal_eval(data)
				f.close()

	for key, value in dictionary.items(): 
		not_word = []
		words = []
		for v in value: 
			words.append(v)
			if v not in exclude and v not in stop: 
				not_word.append(v)
		#print(not_word)
		#get_pos(words)
		get_pos(not_word,key)


def get_pos(pun,key):
	#for p in pun: 
	pun_sent = ' '.join(pun)

	dictionary=PyDictionary()
	sen = sp(pun_sent)


	# FOR TASK TWO ---> PUN IS HAS HIGHEST SIMILARITY
	for i in sen:
		print(i)
		for j in sen: 
			#print('Similarity with ',i,' and ',j, ': ',i.path_similarity(j))
			print('Similarity with ',i,' and ',j, ': ',i.similarity(j))
			#print("Similarity:", sen2.similarity(i))
	
def main():
	# parse xml file
	directory = 'semeval2017_task7/data/trial'

	subtask1 = {}
	hetero = []
	homo = []
	for filename in os.listdir(directory):
	    f = os.path.join(directory, filename)
	    if os.path.isfile(f):
	    	name = os.path.splitext(filename)[0]
	    	if name.startswith("subtask2"):
	    		if 'heterographic' in name: 
	    			hetero.append(f)
	    		if 'homographic' in name: 
	    			homo.append(f)

	subtask1['heterographic'] = hetero
	subtask1['homographic'] = homo


	pos_homographic(subtask1['homographic'])







      
if __name__ == "__main__":
  
    # calling main function
    main()
