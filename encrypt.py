import os
import sys

script = sys.argv[0]
doc = sys.argv[1]
result = doc + ".encrypt"


fo1 = open(doc, "r")
fo2 = open(result, "w")


# Write any algo. to scramble data
for line in fo1.readlines():
	for char in line:
		fo2.write(chr(ord(char) + 1))


	

