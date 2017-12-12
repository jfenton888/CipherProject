import sys
from finalc import caesar #Importing classes from classes file names finalc
from finalc import morse
f = open('workfile', 'w') #Opens new text file


response0 = str(input("What phrase will we be dealing with? ")) #Asks for message

response1 = input("Would you like to encrypt[1] or decrpt[2]? ")

if response1 == "1":
	response11 = input("What language would you like encrypt in to? [1]Caesar [2]Morse [3]Letter Shift: ")
	if response11 == '1':
		response00 = int(input("How many times do we want to shift it? "))
		caesar1 = caesar(response00, response0)
		#caesar1.show_encrypt()
		f.write("Initial input: " + response0+".\n") #Wrties initial input and then goes to next line
		f.write("Enecrypted into caesar.\n")
		f.write("Decrypted phrase: " + str(caesar1.show_encrypt())+"\n") # Shows decrpted phrase as a string

	if response11 == '2':
		morse1 = morse(response0)
		morse1.correspond1()
		f.write("Initial input: " + response0+".\n")
		f.write("Enecrypted into morse.\n")
		f.write("Decrypted phrase: " + str(morse1.correspond1())+"\n")

	if response11 == '3':
		pass


elif response1 == "2":
	response2 = input("What language would you like to decrpt? [1]Caesar [2]Morse [3]Letter Shift: ")

	if response2 == '1':
		response00 = int(input("How many times do we want to shift it? "))
		caesar1 = caesar(response00, response0)
		#caesar1.show_decrypt()
		f.write("Initial input: " + response0+".\n")
		f.write("Decrypted out of caesar.\n")
		f.write("Decrypted phrase: " + str(caesar1.show_decrypt())+"\n")

	if response2 == '2':
		morse1 = morse(response0)
		f.write("Initial input: " + response0+".\n")
		f.write("Decrypted out of morse.\n")
		f.write("Decrypted phrase: " + str(morse1.correspond2())+"\n")

	if response2 == '3':
		pass

f.close() #Closes access to text file
