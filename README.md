# ENLP-Final-Project
Pun Detection: https://alt.qcri.org/semeval2017/task7/

can look into using

	The number of words that are predicted differently if one word ω is masked, using BERT.
	
	the pun word is usually in second half of the phrase. Get pos of words in the sentence, then look at the second half, get rid of any stop words/punctiation. Then look at the remining words and their defintions? 

**SUBTASK 1 ----> PUN DETECTION**

	Homographic Puns: 
		these are puns that are the same word but different meanings. 

			Look into PoS and then look at the defintions and can elminate words that have only 1. 
			Can get rid of stop words in this case. 

			- Take last word, if definition for the PoS it was tagged as has more than one meaning. 
				If it has more than one meaning --> there is a Pun 
				If not (or the defintion doesnt exist) --> no pun 
					total correct: 
					precision: 
					recall:
					f1: 
					accuracy:  0.5613333333333334

			- **Next step** look at the other words in the sentence 
				This will allow us to get a better read at whether or not there is a pun 
				How do we do it?
	Hetergraphic Puns: 
		these are puns that sound similar. 

			Can look into PoS but it might not be helpful 

			can also look ar definitions 
		
		word similarity would work
		
		can look at sense of words -- see if there is something that looks for similar sounding words????
		
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


