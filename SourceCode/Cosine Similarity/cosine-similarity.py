import re
import sys
import json
import pickle
import math

#Argumen check
if len(sys.argv) < 4 :
	print ("\n\nPenggunaan\n\tquery.py [index] [n] [query]..\n")
	print(len(sys.argv))
	sys.exit(1)

if len(sys.argv) > 4:

	sum=3
	query=[]
	len = len(sys.argv) - 3
	for i in range(len):
		key = sys.argv[sum+i].split(" ")
		query.extend(key)

else:
	query = sys.argv[3].split(" ")

n = int(sys.argv[2])

with open(sys.argv[1], 'rb') as indexdb:
	indexFile = pickle.load(indexdb)

#query
list_doc = {}
list_query = {}
bobot_query = {}

for q in query:
	if q in list_query:
		list_query[q] += 1
	else:
		list_query[q] = 1

#Menghitung nilai bobot query
for k, v in list_query.items():
	for doc in indexFile[k]:
		tmp = (v / doc['tf_it']) ** 2
		doc['bobot_query'] = math.sqrt(tmp)
		doc['sukmadq'] = doc['bobot_term'] / doc['tf_it']
		
#Menjumlahkan Bobot Query
for q in query:
	try :
		for doc in indexFile[q]:
			if doc['url'] in list_doc:
				list_doc[doc['url']]['bobot_term'] += doc['bobot_term']
				list_doc[doc['url']]['sukmadq'] += doc['sukmadq']
				
				if list_query[q] == 1:
					list_doc[doc['url']]['bobot_query'] += doc['bobot_query']
				else:
					list_doc[doc['url']]['bobot_query'] = doc['bobot_query']
			else :
				list_doc[doc['url']] = doc
	except :
		continue

#Menghitung Cosine Similiarity
for q in list_doc:
	list_doc[q]['Cossim'] = list_doc[q]['sukmadq'] / (list_doc[q]['bobot_query'] * list_doc[q]['akarsukmaw2'])
	#print(list_doc[q]['Cossim'])

#convert to list
list_data=[]
for data in list_doc :
	list_data.append(list_doc[data])

#sorting list descending
count = 1
for data in sorted(list_data, key=lambda k: k['Cossim'], reverse=True):
	y = json.dumps(data)
	print(y)
	print("\n")
	if (count == n) :
		break
	count+=1

