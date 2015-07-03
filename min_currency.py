#Function to provide minimum no.of currency notes to a given amount.
def notes(amount):

	th=amount/1000
	amount=amount%1000
	print "No. of 1000's:", th

	fh=amount/500
	amount=amount%500
	print "No. of 500's :",fh

	hn=amount/100
	amount=amount%100
	print "No. of 100's :",hn

	fi=amount/50
	amount=amount%50
	print "No. of 50's  :",fi

	tw=amount/20
	amount=amount%20
	print "No. of 20's  :",tw

	tn=amount/10
	amount%=10
	print "No. of 10's  :",tn

	fv=amount/5
	amount%=5
	print "No. of 5's   :",fv

	two=amount/2
	amount%=2
	print "No. of 2's   :",two

	one=amount/1
	amount%=1
	print "No. of 1's   :",one


rupees=int(raw_input("Enter amount:"))
notes(rupees)
