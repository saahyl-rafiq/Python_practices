
"""
#Read from terminal using argument vector
from sys import argv
script,filename=argv
text=open(filename)
print text.read()
"""

print "Enter file name to open:"
user_file=raw_input()
o_u_file1=open(user_file)
ftext=o_u_file1.read()
#print o_u_file1.name
print ftext
