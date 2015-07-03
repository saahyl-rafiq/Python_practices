import json
import csv

#loading json from file
with open ('employee.json','r') as fpj:
	d=json.load(fpj)

#Traversing {dictionary of [list of {dictionaries}]}	
#	print d,type(d), d.keys() 
#	for l in d["employees"]:
#		print l["firstName"]
#		print l["lastName"]

#writing json to csv
header =["firstName","lastName"]
with open ('empjson.csv', 'wb+') as fpw:
	csv_writer=csv.writer(fpw)
	csv_writer.writerow(header)
	for l in d["employees"]:
		csv_writer.writerow([l["firstName"],l["lastName"]])





