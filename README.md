# ENLP-Final-Project
Pun Detection: https://alt.qcri.org/semeval2017/task7/

can look into using

	The number of words that are predicted differently if one word ω is masked, using BERT.
	
	the pun word is usually in second half of the phrase. Get pos of words in the sentence, then look at the second half, get rid of any stop words/punctiation. Then look at the remining words and their defintions? 


Looking at word similarity with in the sentence. 
Unsure what to do with the two puns that in quotes.... 
  - "I ate the soap" , Tom lied.
  - "Quick, dive into those reeds!" Tom rushed. 

'I used to be a banker but I lost interest' --> used banker lost interest
	
	banker is the subject
	
	check similarity of other words against the subject
		highest similarity is INTEREST (0.41) 
		
	
'When the church nought gas for the barbecue, proceeds went from sacred to the propane.' --> church bought gas annual barbecue proceeds went sacred propan
	
	church is the subject
	
	check similarity of other words against the subject
		highest similarity is PROPANE (0.41) 


