#Function to check for prime
def prime(num):
	flag=0
	for i in range(2,num):
		if num % i !=0:
			flag=0
		else:
			flag=1
			break

	if flag==0:
		#print "prime"
		return "%d is Unique and prime" % num
	else:
		#print "Unique num %d is not prime" % num
         return "Unique num %d is not prime" % num

#prime(10)

# Enter numbers to a list 
elements=raw_input('enter elements:')
elements=elements.split(' ')
element_count=[]

#Take count of elements in a list into another list
for e in elements:
	element_count.append(elements.count(e))

for r in range(0,len(element_count)):
#Check for uniqueness in the list
	if element_count[r]==1:
		unique=int(elements[r])
		print prime(unique)
		
	





