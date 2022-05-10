import pandas as pd
import os, ast, string, filecmp
import spacy
import argparse
import phones

from PyDictionary import PyDictionary
from pprint import pprint
from nltk.corpus import stopwords 
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import wordnet as wn

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from SoundsLike.SoundsLike import Search
from collections import Counter
from nltk.stem.wordnet import WordNetLemmatizer

sp = spacy.load('en_core_web_sm')
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
dictionary=PyDictionary()

def homographic(subtask1_homographic,name,model):
	#print(subtask1_homographic)

	for i in subtask1_homographic: 
		if i.endswith("puns.txt"): 
			#print(i)
			with open(i, 'r') as f:
				data = f.read()
				dictionary = ast.literal_eval(data)
				f.close()

	answers = []
	for key, value in dictionary.items(): 
		not_word = []
		words = []
		for v in value: 
			words.append(v)
			if v.lower() not in exclude and v.lower() not in stop: 
				not_word.append(v)

		answers = dic(words, not_word,key,answers)

	file = open('semeval2017_task7/data/'+model+'/'+name+'_predicted.txt', 'w')
	
	for element in answers: 
		file.write(element+'\n')
	file.close()


#looks at only the POS and definitions 
#if a word has mutliple definitons for its tagged POS then it might be the pun
def dic(full_sent,pun,key,answers):

	
	pun_sent = ' '.join(full_sent)
	lemma = WordNetLemmatizer() 
	normalized = " ".join(lemma.lemmatize(word,'v') for word in pun_sent.split()) 

	#print(normalized)
	sen = sp(normalized)
	#sen = sp(pun_sent)

	print('KEY # ', key)
	#print(full_sent)

	check_pun = []
	
	for w in sen:
		lemma_list = []
		count_def = 0
		#definition = dictionary.meaning(str(w))
		
		if w.pos_ == 'VERB':
			pos = 'v'
		elif w.pos_ == 'ADV' or w.pos_ == 'ADP' or w.pos_ == 'INTJ':
			pos='r'
		elif w.pos_ == 'NOUN' or w.pos_ == 'PROPN' or w.pos_ == 'PRON':
			pos='n'
		elif w.pos_ == 'ADJ':
			pos='a'
		else: 
			pos = 'none'
	

		if pos != 'none':
			#print(w)
			for synset in wn.synsets(str(w), pos):
				for lemma in synset.lemmas():
				    lemma_list.append(str(lemma.name()))

			counts = Counter(lemma_list)
			count_w = counts[str(w)]
			

			if count_w > 5:
				definition = dictionary.meaning(str(w))
				if definition != None:
					if len(definition) > 1:
						if pos == 'v': 
							if 'Verb' in definition.keys():
								count_def = len(definition['Verb'])
							else:
								count_def = 0
						elif pos == 'n': 
							if 'Noun' in definition.keys():
								count_def = len(definition['Noun'])
							else:
								count_def = 0
						elif pos == 'a': 
							if 'Adjective' in definition.keys():
								count_def = len(definition['Adjective'])
							else:
								count_def = 0
						elif pos == 'r': 
							if 'Adverb' in definition.keys():
								count_def = len(definition['Adverb'])
							else:
								count_def = 0
				else:
					count_def = 0


		if count_def > 1: 
			check_pun.append(1)
			answers.append(str(key)+'\t1')
			print(str(key)+'\t1')
			break
		else:
			check_pun.append(0)


	
	if 1 not in check_pun: 
		answers.append(str(key)+'\t0')
		print(str(key)+'\t0')
		

	return answers


def compare(directory): 
	for filename in os.listdir(directory):
	    f = os.path.join(directory, filename)
	    if os.path.isfile(f):
	    	name = os.path.splitext(filename)[0]
	    	if name.startswith("subtask1-homographic"):
		    	if f.endswith("predicted.txt"):
		    		predicted = f
	    		if f.endswith("gold"):
		    		gold = f

	precision,recall,f1,accuracy= getCorrect(gold, predicted)
	print("Precision: ",precision)
	print("Recall: ",recall)
	print("F1: ",f1)
	print("Accuracy: ",accuracy)


def getCorrect(gold, predicted):

	with open(gold, 'r') as file:
		gold_answers = file.readlines()
	file.close()
	with open(predicted, 'r') as f:
		predicted_answers = f.readlines()
	f.close()

	print(gold_answers)
	count = 0  
	for i in range(len(gold_answers)):
		if gold_answers[i] == predicted_answers[i]: 
			count +=1


	print(count, ' out of ', len(gold_answers), ' are correct')

	
	precision = precision_score(gold_answers, predicted_answers, average=None)
	recall = recall_score(gold_answers, predicted_answers, average=None)
	f1 = f1_score(gold_answers, predicted_answers, average=None)
	accuracy = accuracy_score(gold_answers, predicted_answers)


	return precision,recall,f1,accuracy

def main(args):
	# parse xml file

	model = args.model
	directory = 'semeval2017_task7/data/'+model

	subtask1 = {}
	hetero = []
	homo = []
	for filename in os.listdir(directory):
	    f = os.path.join(directory, filename)
	    if os.path.isfile(f):
	    	name = os.path.splitext(filename)[0]
	    	if name.startswith("subtask1"):
	    		if 'heterographic' in name: 
	    			hetero.append(f)
	    		if 'homographic' in name: 
	    			homo.append(f)

	subtask1['heterographic'] = hetero
	subtask1['homographic'] = homo

	homographic(subtask1['homographic'],name,model)
	#heterographic(subtask1['heterographic'],name,model)

	compare(directory)

      
if __name__ == "__main__":
  
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--model', help='trial or test', required = True)

    args = parser.parse_args()
    main(args)







