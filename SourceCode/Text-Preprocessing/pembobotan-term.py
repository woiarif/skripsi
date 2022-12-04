import json
import math
import pickle

with open('tes', 'rb') as f:
    data = pickle.load(f)

bobot_dokumen = {}
for k in data:
    #print(k)
    for index in range(len(data[k])):
        #print(data[k][index])
        tmp = 0
        data[k][index]['bobot_term'] = data[k][index]['tf_dt'] / data[k][index]['tf_it']

        tmp = data[k][index]['bobot_term'] ** 2

        if data[k][index]['url'] in bobot_dokumen:
            bobot_dokumen[data[k][index]['url']] += tmp
        else:
            bobot_dokumen[data[k][index]['url']] = tmp

for k in data:
    print("sekarang proses ",k)
    for index in range(len(data[k])):
        data[k][index]['akarsukmaw2'] = math.sqrt(bobot_dokumen[data[k][index]['url']])

'''''
with open('output.json', 'w') as output_file:
    json.dump(data, output_file)
'''''
with open('tess', 'wb') as file:
    pickle.dump(data, file)

