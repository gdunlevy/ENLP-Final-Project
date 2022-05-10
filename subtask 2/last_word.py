import pandas as pd
import os, ast, string, filecmp
import spacy
import argparse
import random 


from PyDictionary import PyDictionary
from pprint import pprint
from nltk.corpus import stopwords 
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import wordnet as wn

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from SoundsLike.SoundsLike import Search
from collections import Counter
from nltk.stem.wordnet import WordNetLemmatizer
import statistics

sp = spacy.load('en_core_web_sm')
stop = set(stopwords.words('english'))
exclude = set(string.punctuation)

def homographic(subtask2_homographic,name,model):
	
	for i in subtask2_homographic: 
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
			words.append(v.lower())
			if v.lower() not in exclude: #and v.lower() not in stop: 
				not_word.append(v.lower())

		answers = last_word(not_word,key,answers)
		#answers = last_word_clean(words,key,answers)
		

	file = open('semeval2017_task7/data/'+model+'/'+name+'_predicted.txt', 'w')
	
	for element in answers: 
		file.write(element+'\n')
	file.close()

def last_word(pun,key,answers):
	last_word = pun[-1]

	last_index = pun.index(last_word)
	print(str(key)+'\t'+str(key)+'_'+str(last_index))
	answers.append(str(key)+'\t'+str(key)+'_'+str(last_index))

	return answers

def last_word_clean(pun,key,answers):
	'''

	loop through the pun list backwards
	if the last thing is NOT a stop word or a punctuation 
		then that is the pun

	'''
	for i in reversed(pun) :
		if i.lower() not in exclude and i.lower() not in stop:
			index = pun.index(i)

			print(str(i) + '\t'+str(index)+'\t'+str(len(pun)))

			answers.append(str(key)+'\t'+str(key)+'_'+str(index))
			break
	return(answers)


def compare(directory): 
	for filename in os.listdir(directory):
	    f = os.path.join(directory, filename)
	    if os.path.isfile(f):
	    	name = os.path.splitext(filename)[0]
	    	if name.startswith("subtask2-homographic"):
		    	if f.endswith("predicted.txt"):
		    		predicted = f
	    		if f.endswith(".gold"):
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

	count = 0  
	for i in range(len(gold_answers)):
		if predicted_answers[i] in gold_answers[i]: 
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

	subtask2 = {}
	hetero = []
	homo = []
	for filename in os.listdir(directory):
	    f = os.path.join(directory, filename)
	    if os.path.isfile(f):
	    	name = os.path.splitext(filename)[0]
	    	if name.startswith("subtask2"):
	    		if 'homographic' in name: 
	    			homo.append(f)

	subtask2['homographic'] = homo

	homographic(subtask2['homographic'],'subtask2-homographic',model)

	compare(directory)

      
if __name__ == "__main__":
  
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--model', help='trial or test', required = True)

    args = parser.parse_args()
    main(args)


