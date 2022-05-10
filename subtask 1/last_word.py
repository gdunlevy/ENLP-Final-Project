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

		answers = get_pos_last_word(not_word,key,answers)
		

	file = open('semeval2017_task7/data/'+model+'/'+name+'_predicted.txt', 'w')
	
	for element in answers: 
		file.write(element+'\n')
	file.close()
  
#a basline -- just checking if the last word is the pun based off of its defintion count (like dic())
def get_pos_last_word(pun,key,answers):
		
	pun_sent = ' '.join(pun)
	dictionary=PyDictionary()
	sen = sp(pun_sent)

	print('KEY # ', key)

	#Take last word, and check to see if there are more than one def. Then for the pos if the pos has more than one
	count_def = 0
	last_word = sen[-1]
	definition = dictionary.meaning(str(last_word))
	if definition != None: 
		print(len(definition))
		print(definition)
		if len(definition) > 1:
			#print(f'{last_word.text:{12}} {last_word.pos_:{10}} {last_word.tag_:{8}} {spacy.explain(last_word.tag_)}')
			print(last_word.pos_)
			print(last_word)
			
			if last_word.pos_ == 'VERB':
				if 'Verb' in definition.keys():
					count_def = len(definition['Verb'])
					#print(wn.synsets(str(w), pos='v'))
				
			elif last_word.pos_ == 'ADV' or last_word.pos_ == 'ADP' or last_word.pos_ == 'INTJ':
				if 'Adverb' in definition.keys():
					count_def = len(definition['Adverb'])
					#print(wn.synsets(str(w), pos='b'))
	
			elif last_word.pos_ == 'NOUN' or last_word.pos_ == 'PROPN' or last_word.pos_ == 'PRON':
				if 'Noun' in definition.keys():
					count_def = len(definition['Noun'])
				
			elif last_word.pos_ == 'ADJ':
				if 'Adjective' in definition.keys():
					count_def = len(definition['Adjective'])



	if count_def > 1: 
		answers.append(str(key)+'\t1')
		print(str(key)+'\t1')

	else: 
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
	    		if 'homographic' in name: 
	    			homo.append(f)

	subtask1['homographic'] = homo

	homographic(subtask1['homographic'],name,model)

	compare(directory)

      
if __name__ == "__main__":
  
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--model', help='trial or test', required = True)

    args = parser.parse_args()
    main(args)








