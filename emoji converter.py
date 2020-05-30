message = input('>')
words = message.split(' ')
emojis = {
	':)' : '😃',

	':(' : '☹️', 

	'<3' : '❤️', 
 
}

output = ''
for word in words:
	output += emojis.get(word, word) + ' '

print (output)
