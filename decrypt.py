import os
import sys

script = sys.argv[0]
doc = sys.argv[1]

#  H  E  L  L  O
#  0  1  2  3  4
# -5 -4 -3 -2 -1
#
# Considering only first len(doc) - 8 charecters
result = doc[:-8]


fo1 = open(doc, 'r')				# encrypted version
fo2 = open(result, 'w')				# decrypted version


# write algo. to decrypt file encrypted by encrypt.py
for line in fo1.readlines():
	for char in line:
		fo2.write( chr(ord(char) - 1) )

