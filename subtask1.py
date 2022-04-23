import pandas as pd
import os, ast, string, filecmp
import spacy

from PyDictionary import PyDictionary
from pprint import pprint
from nltk.corpus import stopwords 
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import wordnet as wn

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score


sp = spacy.load('en_core_web_sm')
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)


def heterographoc(subtask1_heterographic,name):

	print('idk')


	'''
	not sure what to do here yet
	this is for puns for words that sounds similar (profane --> propane)


	look at similarity of words?
	look at definintions?


	need ideas for this 
	'''

def homographic(subtask1_homographic,name):
	print (subtask1_homographic)


	for i in subtask1_homographic: 
		if i.endswith("puns.txt"): 
			print(i)
			#df = pd.read_csv(i)
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
			if v not in exclude and v not in stop: 
				not_word.append(v)
		#print(not_word)
		#get_pos(words)
		answers = get_pos(not_word,key,answers)

	file = open('semeval2017_task7/data/trial/'+name+'_predicted.txt', 'w')
	
	for element in answers: 
		file.write(element+'\n')
	file.close()


def get_pos(pun,key,answers):
	#for p in pun: 
	pun_sent = ' '.join(pun)
	dictionary=PyDictionary()
	sen = sp(pun_sent)

	#Take last word, and check to see if there are more than one def. Then for the pos if the pos has more than one

	last_word = sen[-1]
	definition = dictionary.meaning(str(sen[-1]))
	
	if definition != None: 
		if len(definition) > 1: 
			#print(f'{last_word.text:{12}} {last_word.pos_:{10}} {last_word.tag_:{8}} {spacy.explain(last_word.tag_)}')

			if last_word.pos_ == 'VERB':
				count_def = len(definition['Verb'])
			if last_word.pos_ == 'NOUN':
				count_def = len(definition['Noun'])
			if last_word.pos_ == 'ADJ':
				count_def = len(definition['Adjective'])
			
			if count_def > 1: 
				answers.append(str(key)+'\t1')
			else: 
				answers.append(str(key)+'\t0')

	return answers


def compare(directory): 
	for filename in os.listdir(directory):
	    f = os.path.join(directory, filename)
	    if os.path.isfile(f):
	    	name = os.path.splitext(filename)[0]
	    	if name.startswith("subtask1"):
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
	gold_answers = []
	predicted_answers = []

	with open(gold, 'r') as file:
		data_g = file.read()
		gold_answers.append(data_g)
	file.close()
	with open(predicted, 'r') as f:
		data_p = f.read()
		predicted_answers.append(data_p)
	f.close()

	
	precision = precision_score(gold_answers, predicted_answers, average=None)
	recall = recall_score(gold_answers, predicted_answers, average=None)
	f1 = f1_score(gold_answers, predicted_answers, average=None)
	accuracy = accuracy_score(gold_answers, predicted_answers)


	return precision,recall,f1,accuracy

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
	    	if name.startswith("subtask1"):
	    		if 'heterographic' in name: 
	    			hetero.append(f)
	    		if 'homographic' in name: 
	    			homo.append(f)

	subtask1['heterographic'] = hetero
	subtask1['homographic'] = homo


	homographic(subtask1['homographic'],name)

	compare(directory)

      
if __name__ == "__main__":
  
    # calling main function
    main()
