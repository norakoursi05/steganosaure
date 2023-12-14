import string

def cesar_ciffer(message, key):
	if type(key) != int :
		print("la clef doit être un entier")
		return None

	message = str(message)

	list_of_crypted_caracs = []
	
	for carac in message:
		crypted_index = (string.printable.index(carac) + key) % len(string.printable)
		crypted_carac = string.printable[crypted_index]
	
		list_of_crypted_caracs.append(crypted_carac)
	
	crypted_message = "".join(list_of_crypted_caracs)

	return crypted_message

def cesar_decrypt(crypted_message, key):
	return cesar_ciffer(crypted_message, -key)

crypted_message = cesar_ciffer("j'ai envie de manger gratin de pates avec des lardons", 762)

print(crypted_message)
print(cesar_decrypt(crypted_message, 762))


print("Je suis un hacker")
print("#"*30)
for possible_key in range(0, len(string.printable)):
	print(cesar_decrypt(crypted_message, possible_key))
print("#"*30)
