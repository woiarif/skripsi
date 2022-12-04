from itertools import count
import re
import sys
import json
import pickle
import math
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from traceback import print_tb
import time
import json
import nltk
from nltk.corpus import stopwords
import pandas as pd
start_time = time.time()

#Argumen check
if len(sys.argv) !=3 :
	print ("\n\\Use python \n\t pre-processing.py [data.json] [output]\n")
	sys.exit(1)

#data argumen
input_data = sys.argv[1] #data.json
output_data = sys.argv[2] #output / indexdb

data = open(input_data, encoding="mbcs").read() #membuka data json
list_data = data.split("\n") #memisahkan menggunakan \n


content=[]
for x in list_data :
	try:
		content.append(json.loads(x)) #menambahkan data json yg sudah dipisah ke content
	except:
		continue

#Tahap Case Folding dan Tokenizing
def case_folding(text): 									
	text = text.lower()										
	text = (text.encode('ascii', 'ignore')).decode("utf-8")	#
	text = re.sub("&.*?;", "", text)
	text = re.sub("\.+", "", text)
	text = re.sub("^\s+","" ,text)
	text = re.sub("\2013", "",text)
	text = re.sub(r'[^\w\s]', "", text)
	text = re.sub(' +', " ", text)
	text = re.sub(r'[0-9]+', "", text)
	text = text.strip()
	return text

for data in content: #Looping data pada array Content 
	text_data = case_folding(data['text']) #Mengirim setiap text ke Method Case Folding
	list_word = text_data.split(" ")

#Tahap Stop-Word Removal
sw = set(stopwords.words("indonesian"))

#Tahap Stemming
def stemming(text):
	factory = StemmerFactory()
	stemmer = factory.create_stemmer()
	output = stemmer.stem(text)
	return output

tf_it={}
tf_data={}
idf_data={}
data_text = []

i=0;
itung=0
for idx, data in enumerate(content) :
	
	tf={} 
	#susun per kata
	clean_text = case_folding(data['text'])
	clean_text = stemming(clean_text)
	itung+=1
	print('Dokumen ke-',itung)
	
	list_word = clean_text.split(" ")
	data_text.append(" ". join(list_word) if len(list_word) < 20 else " ". join([list_word[i] for i in range(20)]))
	
	for word in list_word :
		if word in sw:
			continue
		
		#jumlah tf per dokumen (tf_dt)
		if word in tf :
			tf[word] += 1
		else :
			tf[word] = 1

		#jumlah tf_it
		if word in tf_it :
			tf_it[word] += 1
		else :
			tf_it[word] = 1


	tf_data[data['url']] = tf
	
print("\nJumlah Kata di tf_it:", len(tf_it))	
tf_ti_weight = {}


hitung_kata = 0
for word in tf_it:
	hitung_kata +=1
	print("Kata ke-",hitung_kata,' Dari', len(tf_it))
	list_doc = []
	for idx, data in enumerate(content):
		
		tf_dt = 0
		if word in tf_data[data['url']]:
			tf_dt = tf_data[data['url']][word] #TF(d,t)

		doc = {
			'url' : data['url'],
			'image' : data['image'],
			'title' : data['title'],
			'text' : data_text[idx],
			'bobot_term' : 0,
			'tf_dt' : tf_dt,
			'tf_it' : tf_it[word],
			'Cossim' : 0,
			'sukmadq' : 0,
			'bobot_query' : 0,
			'akarsukmaw2' : 0
		}
		if doc['tf_dt'] != 0 :
			if doc not in list_doc:
				list_doc.append(doc)
	tf_ti_weight[word] = list_doc


"""""""""
with open(output_data+'.json', 'w') as output_file:
    json.dump(tf_ti_weight, output_file)

"""""""""
with open(output_data, 'wb') as file:
    pickle.dump(tf_ti_weight, file)


print("\nDurasi Running: %s seconds" % (time.time() - start_time))
print("Jumlah Term:", hitung_kata)
print("Jumlah Dokumen:", itung,"\n")