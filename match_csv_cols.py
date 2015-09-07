# Script to write rows to new csv files when:
#  i)Only the record_id but NOT the hcp_id of the corresponding rows of 2 files matches,
# ii)There are more no. of rows in one file than the other write them to a separate file.

import csv

with open('scriptcsv1.csv','rb') as csv1:
	csv1reader=csv.reader(csv1)
	header1=next(csv1reader)
	rec_id1=header1.index('record_id')
	hcp_id1=header1.index('hcp_id')

	with open('scriptcsv2.csv','rb') as csv2:
		csv2reader=csv.reader(csv2)
		header2=next(csv2reader)
		rec_id2=header2.index('record_id')
		hcp_id2=header2.index('hcp_id')

		rec1=[row for row in csv1reader]
		rec2=[row for row in csv2reader]
		l=min(len(rec1),len(rec2))
        
        # If only record_id but not the hcp_id of the corresponding rows of 2 files matches write them to hcpidnomatch.csv file
		with open('hcpidnomatch.csv','wb')as csv4w:
			csv4writer=csv.writer(csv4w)

			for  i in range(0,l):
				if rec1[i][rec_id1]==rec2[i][rec_id2] and rec1[i][hcp_id1]!=rec2[i][hcp_id2]:
					print "rec_id1 rec_id2 hcp_id1 hcp_id2\n %-6s %-7s %-7s %-6s " % (rec1[i][rec_id1],rec2[i][rec_id2],rec1[i][hcp_id1],rec2[i][hcp_id2])									
					csv4writer.writerow(rec2[i])

		# If rec1 has more rows write them to extrarec.csv file
		if len(rec1)>l:
			with open('extrarec.csv','wb')as csv3w:
				csv3writer=csv.writer(csv3w)
				for i in range(l,len(rec1)):
					csv3writer.writerow(rec1[i])

        # If rec2 has more rows write them to extrarec.csv
		elif len(rec2)>l:
			with open('extrarec.csv','wb')as csv3w:
				csv3writer=csv.writer(csv3w)
				for i in range(l,len(rec2)):
					csv3writer.writerow(rec2[i])




