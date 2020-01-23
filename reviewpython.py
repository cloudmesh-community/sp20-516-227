import os
import json


os.system("system_profiler -json SPMemoryDataType SPStorageDataType > /Users/xingu/Documents/E516/computer_profile.json")

with open('/Users/xingu/Documents/E516/computer_profile.json', 'r') as myfile:
    data=myfile.read()
obj = json.loads(data)

memory = int(obj['SPMemoryDataType'][0]['_items'][0]['dimm_size'].strip(' GB')) + int(obj['SPMemoryDataType'][0]['_items'][1]['dimm_size'].strip(' GB'))

storage = obj['SPStorageDataType'][0]['size_in_bytes']/1073741824 + obj['SPStorageDataType'][1]['size_in_bytes']/1073741824

print(f"Computer Memory is {memory} GB")
print(f"Computer HDD is {int(storage)} GB")