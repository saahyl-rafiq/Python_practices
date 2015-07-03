import csv
with open('testcsv.csv','rb') as fp:
	r=csv.reader(fp)
	rownum=0
	for row in r:
		#Get the attributes into a list
		if rownum==0:
			header=row
			#print type(row)
			#print type (header)
			#print header
		else:
			colnum=0

			for col in row:
				print "%-10s: %s" %(header[colnum], col)
				colnum+=1

		rownum+=1

