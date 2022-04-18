import os 
import pandas as pd
import spacy
from PyDictionary import PyDictionary
from pprint import pprint

sp = spacy.load('en_core_web_sm')

def read(f): 
	df = pd.read_csv(f)
	words = []

	for index, row in df.iterrows(): 
		for col in df.columns: 
			column = col
		words.append(str(row[column]))


	sentence = ' '.join(str(w) for w in words)

	return (sentence)


def pos(sentence): 

	dictionary=PyDictionary()
	sen = sp(sentence)
	for word in sen:
		print(word)

		print(f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}')
		

		
		#if word.pos_ == 'DET' or word.pos_ == 'CCONJ' or word.pos_ == 'PUNCT' or word.pos_ =='PART': 
		definition = dictionary.meaning(str(word))
		print(definition)

		'''
		if word.pos_ == 'PRON' or word.pos_ == 'NOUN'or word.pos_ == 'PROPN' and keys == 'Noun':
			pprint(definition['Noun'])
		exit()
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
	    	if f.endswith((".csv")):
	    		#name = os.path.splitext(filename)[0]
	    		sentence = read(f)
	    		pos(sentence)
	    		exit()




      
if __name__ == "__main__":
  
    # calling main function
    main()
