#!/usr/bin/env python
import datetime

'''
python dictionaries
list Comprehension 

''' 
someDict = {}
myDict = {'name': None, "last_name": None, "phone_num": None }

myDict['name'] = "krishna"








myDict["last_name"] = "guntuka"

print(myDict) 
myDict['name'] = "himagiri"

for item in myDict:
   print(item) 


for item in myDict:
   print(myDict[item])

for key, value in myDict.items():
   print(key)
   print(value)

for values in myDict.values():
   print(values)

print(myDict.keys())

print(myDict.values())


print(len(myDict))

if "guntuka" in myDict.values():
    print("TRUE")

if "name" in myDict:
    print("FALSE")
else:
    print("TRUE")

print(datetime.datetime.now())
