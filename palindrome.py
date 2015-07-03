def palin():
	line=raw_input('Enter a string:')
	lst=line.split(' ')
	for i in lst:
		if i==i[::-1]:
			print "Palindrome: %r == %r " % (i, i[::-1])
			#print "palindrome:",i "==", i
		else:
			print "Not Palindrome: %r != %r " % (i, i[::-1])
			#print "           ", i "!=", i[::-1]

palin()
		

