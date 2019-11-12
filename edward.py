with open('somefile.txt', 'r') as somefile:
	string_ = somefile.read()
	lst = ['']
	for letter in string_:
		if letter == lst[-1]:
			lst.pop(-1)
			lst.insert(-1,'')
		else:
			lst.append(letter)
			lst.insert(-1,'')
	secret_message = ''.join(lst)
	print(secret_message)


