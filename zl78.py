import numpy as np
import binascii

def find_phrase(databyte,phrases):
	try:
		found = phrases.index(databyte)
		return found
	except ValueError:
		found = False
		return found	


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


phrase_count = 0
phrases = []
address = []
for number in range(4096):
	address.append(format(number,'012b'))
codeword = []

data_length = 0
code_length = 0

f = open("data.txt", "rb")
fout = open("code.txt","w")
databyte = f.read(1)
while databyte:
	index = 0
	new_phrase = format(ord(databyte),'08b')
	found = find_phrase(new_phrase,phrases)
	while (found):
		index = found
		databyte = f.read(1)
		if (databyte):
			new_phrase = new_phrase + format(ord(databyte),'08b')
			found = find_phrase(new_phrase,phrases)
		else:
			found = False
			break
	data_length += len(new_phrase)
	if (databyte):
		phrase_count+=1
		new_codeword = address[index] + format(ord(databyte),'08b')
		print ('Phrase count : ', phrase_count, 'New phrase : ', new_phrase, 'New codeword : ', new_codeword, 'Address : ', address[phrase_count])
		eng = text_from_bits(new_phrase)
		print('New phrase in English : ', eng)
		fout.write(new_codeword)
		phrases.append(new_phrase)
		codeword.append(new_codeword)
		databyte = f.read(1)
	else:
		break
print('Encoding completed...')
for word in codeword:
	code_length += len(word)
efficiency = (1-code_length/data_length) * 100
print('Efficiency is : ', efficiency,'%')
