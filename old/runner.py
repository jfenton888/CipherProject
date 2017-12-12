from AntiquatedMessagingSystem import Cipher
morse = Cipher.MorseCode('hello')
letnum = Cipher.LetterNum('hello')
letshift = Cipher.LetterShift('hello')


response1 = sys.arg("Would you like to translate to[1] or translate back[2]? ")
if response1 == "1":
	response11 = sys.arg("What language would you like translate/encode in to? [1]Morse [2]Letter Number [3]Letter Shift: ")
	if response11 == '1':
		morse.transTo()
	if response11 == '2':
		CipherCode.transTo()
	if response11 == '3':
		SymbolsCode.tranTo()
elif response1 == "2":
	response2 = sys.arg("What language would you like to decode? [1]Morse [2]Letter Number [3]Letter Shift: ")
	if response11 == '1':
		morse.transBack()
	if response11 == '2':
		CipherCode.transBack()
	if response11 == '3':
		SymbolsCode.tranBack()

f = open('workfile', 'w')
f.write()

f.close()