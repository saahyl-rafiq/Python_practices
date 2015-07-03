import csv

with open('testcsv.csv','rb') as fpr:
	r=csv.reader(fpr)
	with open('writecsv.csv','wb+') as fpw:
		w=csv.writer(fpw)

		for row in r:
			w.writerow(row)

with open('writecsv.csv','rb') as fp:
	rw=csv.reader(fp)
	for r in rw:
		print r
		


