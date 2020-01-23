import os
import json
import pprint

os.system("system_profiler -json SPMemoryDataType SPStorageDataType > /Users/xingu/Documents/E516/computer_profile.json")

with open('/Users/xingu/Documents/E516/computer_profile.json', 'r') as myfile:
    data=myfile.read()
obj = json.loads(data)

memory = int(obj['SPMemoryDataType'][0]['_items'][0]['dimm_size'].strip(' GB')) + int(obj['SPMemoryDataType'][0]['_items'][1]['dimm_size'].strip(' GB'))

storage = obj['SPStorageDataType'][0]['size_in_bytes']/1073741824 + obj['SPStorageDataType'][1]['size_in_bytes']/1073741824

computer_info = {"Memory": memory, "Storage":int(storage)}

pprint.pprint(computer_info,width=10, indent=4)
