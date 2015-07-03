print "Enter filename:"
fn=raw_input()
fp=open(fn)
ftext=fp.read()
#ftext=str(ftext)
#ftext=ftext.strip()
#ftext=ftext.splitlines()
print ftext
ftext=ftext.split()

print "Total no. of words:",len(set(ftext))

#Get frequency of words in dictionary
words={}
for word in ftext:
	if word not in words:
		words[word]=1
	else:
		words[word]=words[word]+1
print words

#print "%d is count" % len(words)

total=0
for pair in words:
	total += words[pair]

print "\nTotal frequency of words:  ",total
