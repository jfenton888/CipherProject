#morse code
class MorseCode(inMessage, language):
	"""docstring for MorseCode"""


	def __init__(self, arg):
		self.transTo = transTo
		self.transBack = transBack
		self.send = send
		self.diction = diction


	def transTo():

	def transBack():

	def send():

	def diction():
		diction = [a,b,c]	
				  []


#letters changed
class CypherCode(inMessage, language):



	def __init__(self, arg):
		self.transTo = transTo
		self.transBack = transBack
		self.send = send
		self.diction = diction


	def transTo():
		diction = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		msg = str(input('Please input the text you would like to have translated'))
		MSG = msg.strip().lower()
		NoSPCMSG = nospace(MSG)
		for x in range(len(NoSPCMSG)):
			MSG[x] == diction[x+1]
		return MSG[]






	def transBack():

	def send():

	def diction():
		diction = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
				  

#symbols

work = True
while work==True:
	response1 = sys.arg("Would you like to translate to[1] or translate back[2]? ")
	if response1 = "1":
		response11 = sys.arg("What language would you like translate in to? [1]Morse [2]Cipher [3] Symbols")
			if response11 = '1':
				MorseCode.transTo()
			if response11 = '2':
				CipherCode.transTo()
			if response11 = '3':
				SymbolsCode.tranTo()
	elif response1 ="2":
	response2 = sys.arg("What language ")