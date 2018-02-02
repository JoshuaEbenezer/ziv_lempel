import numpy as np


def find_phrase(databyte,phrases):
	try:
		found = phrases.index(databyte)
		return found
	except ValueError:
		found = False
		return found	


phrase_count = 0
phrases = []
address = []
for number in range(1024):
	address.append("{0:b}".format(number))
codeword = []

data_length = 0
code_length = 0

f = open("data.txt", "rb")
databyte = f.read(1)
index = 0
while databyte:
	new_phrase = "{0:b}".format(ord(databyte))
	data_length += len(databyte)
	found = find_phrase(new_phrase,phrases)
	while (found):
		index = found
		databyte = f.read(1)
		if (databyte):
			new_phrase = new_phrase + "{0:b}".format(ord(databyte))
			found = find_phrase(new_phrase,phrases)
			data_length += len(databyte)
		else:
			found = False
			break

	if (databyte):
		phrase_count+=1
		new_codeword = address[index] + "{0:b}".format(ord(databyte))
		print ('Phrase count : ', phrase_count, 'New phrase : ', new_phrase, 'New codeword : ', new_codeword)
		phrases.append(new_phrase)
		codeword.append(new_codeword)
		databyte = f.read(1)
	else:
		break
print('Encoding completed...')
for word in codeword:
	code_length += len(word)
efficiency = (1-data_length/code_length) * 100
print('Efficiency is : ', efficiency,'%')