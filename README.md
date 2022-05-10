# ENLP-Final-Project
Pun Detection: https://alt.qcri.org/semeval2017/task7/

This project was slipt into two subtask. The first subtask was to determine if a sentence had a pun in it. The second was to determine which word was the pun in the sentence. 
There are two types of puns used: Homographic and Heterographic. 
Homographic --> words that have different meanings but same pronuciation 
	ex: interest
Heterographic --> words that have similar sounding pronunciations
	ex: profane vs. propane

**PARSING CODE**

	parse_data_test.py and parse_data_trial.py
	
	These two files take in the XML files provided by the contest conductors. 
	Because the XML files come pre-labeled, we wanted to fnd a way to make sure we 
	kept those btu also had an easily readable file. 
	We read in the sentences and put them into a dictionary. The key is the sentence tag
	and each word is their own value. We did a dictionary over a dataframe because the 
	dataframe would parse each letter of the word, so when trying to loop through a cell
	you would get it by letter, not the full word. 
	
**SUBTASK 1 ----> PUN DETECTION**
	
	subtask1.py
	
	This file contains the code to preforming some baseline methods for task 1,
	specifically for **HOMOGRAPHIC**. 
	The methods that can be run in this file are: last word, dictionary defintions, 
	and synsets. 
	
	HOMOGRAPHIC:
	- Last word: This is determined by the specific POS definitions of the last words 
	in the sentences. If the last word definition has more than one entry, 
	then we can say there is a pun in that sentence. 
		ex: Weeds (NOUN) --> {'Noun': ['any plant that crowds out 
		cultivated plants', 'a black band worn by a man (on the arm or hat', 
		'street names for marijuana', 'a black garment (dress'], 
		'Verb': ['clear of weeds']} 
	- Dictionary Defitions: This is basically the same as the last word concept but
	it is for every word in the sentence
	-Synset: In this one we use the POS of the word to give us the list of synsets of 
	the word in the sentence. If any word has from the sentence appears in its synset 
	list more than 5 times, then there is a pun in the the sentence. 
	
	HETEROGRAPHIC:
	
		
**SUBTASK 2 ----> WHICH WORD IS THE PUN**
	
	Homographic Puns: 
		these are puns that are the same word but different meanings. 


			- Can say it is the last word just to see the accuracy we get for that

			- how can we find the word in the sentence that is spelt the same but has two totally different meanings 
				- maybe check to see if words have two different PoS and/or multiple definitions for the same PoS


	Hetergraphic Puns: 
		these are puns that sound similar. 

			can look at sense of words -- see if there is something that looks for similar sounding words????

		wordnet sense? not sure


