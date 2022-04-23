import xml.etree.ElementTree as ET
from pprint import pprint
import csv
import os, re
import pandas as pd



def parseXML(rows,name): 

	print(rows)
	s = []
	d = {}
	l = []
	i = 0
	
	#word_index = []
	for row in rows:
		h = ''
		textopen = re.search("<text id",row)
		textclose = re.search("</text>",row)
		sent_id = re.search("<text id=\"[\w]+[\d]+\"",row)

		word = (re.search("\>(.*?)\<",row))

		if textopen:
			s.append(1)
			i+=1
		if sent_id: 
			sent_id = re.search("<text id=\"[\w]+[\d]+\"",row).group(0)
			sentence_index = re.search("[\w]+[\d]", sent_id).group(0)
			#print(sentence_index)
		if s and word:
			
			word = (re.search("\>(.*?)\<",row)).group(1)
			l.append(word)

		if textclose:
			s.pop()
	
			d[sentence_index] = l
			print(d)
			print('...')
			f = open('semeval2017_task7/data/trial/'+name+'_puns.txt', 'w')
			f.write( str(d) )
			f.close()
			#for key, value in d.items():
			#	file1.write('%s:%s\n' % (key, value))
			l = []


	
	#file1 = open('emeval2017_task7/data/trial/'+name+'_puns.txt', 'w')

	'''
	df = pd.DataFrame(d.items(),columns = ['index','Sentence'])
	for index, row in df.iterrows(): 
		for word in row['Sentence']:
			print(word)

	df.to_csv('semeval2017_task7/data/trial/'+name+'puns.csv')

	'''
def to_dict(f,name): 
	mytree = ET.parse(f)
	myroot = mytree.getroot()

	puns = []

	for item in myroot.findall('./text'):

		print(item.attrib['id'])
		dict1 = {}
		dict1[item.attrib['id']] = {}
		#exit()
		# iterate child elements of item
		for child in item:
			idd = child.attrib['id']

			dict1[item.attrib['id']][idd] = child.text.encode('utf8')
		with open('semeval2017_task7/data/trial/dictionary_'+name+'.csv', 'a') as f:
			for key in dict1.keys():
				f.write("%s,%s\n"%(key,dict1[key]))

		puns.append(dict1)

	
def get_rows(f):
	for rows in open(f, "r"):
		yield rows
def main():
    # parse xml file
    directory = 'semeval2017_task7/data/trial'
    for filename in os.listdir(directory):
	    f = os.path.join(directory, filename)
	    # checking if it is a file
	    if os.path.isfile(f):
	    	if f.endswith((".xml")):
	    		name = os.path.splitext(filename)[0]

	    		
	    		rows = get_rows(f)
	    		puns = parseXML(rows,name)
	    		#to_dict(f,name)

	 		      
      
if __name__ == "__main__":
  
    # calling main function
    main()

