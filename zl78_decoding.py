import numpy as np

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


file = open('code.txt','r')
file_out = open('decoded.txt','w')

databyte = file.read(20)
print(databyte[0])
phrase_count = 0

codeword = []
address = []
phrase_asc = []
while(databyte):

	phrase = ''
	# new codeword is what we just read
	codeword.append(databyte)
	# the address that the code is pointing to 
	address.append(databyte[0:12])
	
	# find the index of the codeword that the current code is pointing to
	index = int(address[phrase_count],2)

	# the phrase is at least the end of the current code
	phrase= databyte[12:20]
	
	# it could be longer. Go to code pointed to to find out
	if (index):
		# make the phrase bigger
		phrase = phrase_asc[index] + phrase

	phrase_asc.append(phrase)
	eng_phrase = text_from_bits(phrase)

	print('Codeword : ', codeword[phrase_count], 'Address pointed to : ', address[phrase_count], 'Total phrase : ', eng_phrase)
	
	
	file_out.write(eng_phrase)
	# increment phrase count
	phrase_count += 1

	databyte = file.read(20)


