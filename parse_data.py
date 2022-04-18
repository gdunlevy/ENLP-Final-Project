import xml.etree.ElementTree as ET
from pprint import pprint
import csv
import os
import pandas as pd

def parseXML(xmlfile):
	mytree = ET.parse(xmlfile)
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
		puns.append(dict1)

	return puns

def savetoCSV(puns,name):
  
    # specifying the fields for csv file
    fields = []

    for i in puns: 
    	for k in i.keys():
    		fields.append(k)
    	for item in i.values(): 
    		val = []
    		indexs = []
    		data = {}

    		for key, value in item.items(): 
    			indexs.append(key)
    			val.append(value.decode())

    		data[k] = val

    	#for change in range(len(indexs)):
    	#	indexs[change] = 't_'+str(change)

    	df = pd.DataFrame(data, index = indexs)
    	print(df)

    	df.to_csv('semeval2017_task7/data/trial/'+name+'puns_'+k+'.csv')
    	

#def read():


def main():
    # parse xml file
    directory = 'semeval2017_task7/data/trial'
    for filename in os.listdir(directory):
	    f = os.path.join(directory, filename)
	    # checking if it is a file
	    if os.path.isfile(f):
	    	if f.endswith((".xml")):
	    		name = os.path.splitext(filename)[0]
	    		print(f)
	    		puns = parseXML(f)
	    		savetoCSV(puns,name)
		      
      
if __name__ == "__main__":
  
    # calling main function
    main()
