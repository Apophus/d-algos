"""
Move the first letter of each word to the end of it, 
then add "ay" to the end of the word. Leave punctuation marks untouched.
eg.
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

"""

def pig_it(text):
	split_text = text.split(' ')
	suffix = 'ay'
	res = []
	for char in split_text:
		inner_split = char.split()
		new_arr = list(inner_split[-1]) + inner_split[0:-1]
		if char.isalnum():
			new_str = ''.join(new_arr[1:]) + new_arr[0] + suffix
		else:
			new_str = ''.join(new_arr[1:]) + new_arr[0]
		res.append(new_str)
	
	new_text = ' '.join(res)

	return new_text

text = "O tempora o mores !"


