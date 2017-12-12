
def sendToFile(encodedMessage):
	f = open('messagebank.txt','a')
	f.write('\n' + encodedMessage)
	f.close()

	print('Message Sent!')

class MorseCode:
	def __init__(self):
		self.diction = [[' abcdefghijklmnopqrstuvwxyz0123456789'],[' ', '•– ', '–••• ', '–•–• ', '–•• ', '• ', '••–• ', '––• ', '•••• ', '•• ', '•––– ', '–•– ', '•–•• ', '–– ', '–• ', '––– ', '•––• ', '––•– ', '•–• ', '••• ', '– ', '••– ', '•••– ', '•–– ', '–••– ', '–•–– ', '––•• ', '––––– ', '•–––– ', '••––– ', '•••–– ', '••••– ', '••••• ', '–•••• ', '––••• ', '–––•• ', '––––• ', '']]
		self.outMessage = []

	def transTo(self, inMessage):

		for i in range(len(inMessage)):
			code = (self.diction[1][self.diction[0][0].find(inMessage[i])])
			(self.outMessage).append(code)
		return MorseCode.send()

	def send(self):
		message = ''.join(self.outMessage)
		return message

class LetterNum:
	def __init__(self):
		self.diction = [[' abcdefghijklmnopqrstuvwxyz0123456789'],['0','1','2','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36']]
		self.outMessage = []

	def transTo(self, inMessage):
		print('in LetterNum')
		for i in range(len(inMessage)):
			code = (self.diction[1][self.diction[0][0].find(inMessage[i])])
			(self.outMessage).append(code)
		return LetterNum.send()

	def send(self):
		message = ''.join(self.outMessage)
		return message


class LetterShift:
	def __init__(self):
		self.diction = [[' abcdefghijklmnopqrstuvwxyz0123456789'],[' BCDEFGHIJKLMNOPQRSTUVWXYZ0123456789A']]
		self.outMessage = []

	def transTo(self, inMessage):
		print('in LetterShift')
		for i in range(len(inMessage)):
			code = (self.diction[1][self.diction[0][0].find(inMessage[i])])
			(self.outMessage).append(code)
		return LetterShift.send()

	def send(self):
		message = ''.join(self.outMessage)
		return message

class SymbolCipher:
	def __init__(self):
		self.diction = [[' abcdefghijklmnopqrstuvwxyz0123456789'],[' ','🖯','🖰','🖱','🖲','🖮','🎮','📱','📶','📞','☎','📟','📠','📀','💾','🖫','✇','🖭','🖳','🖥','🖨','🖧','📷','🎥','🎧','🎤','📢','💽','📹','⊗','⊕','🔱','🔭','⚓','🤖','📺','📡', '']]
		self.outMessage = []

	def transTo(self, inMessage):
		print('in SymbolCipher')
		for i in range(len(inMessage)):
			code = (self.diction[1][self.diction[0][0].find(inMessage[i])])
			(self.outMessage).append(code)
		return SymbolCipher.send()

	def send(self):
		message = ''.join(self.outMessage)
		return message


MorseCode = MorseCode()
LetterNum = LetterNum()
LetterShift = LetterShift()
language = '0' 


while (('morse' not in language) and language != '1' and ('l2n' not in language) and language != '2' and ('ls' not in language) and language != '3' and ('sc' not in language) and language != '4'):
	language = (input('What code language do you want your message changed into? \n Morse Code(Morse or 1),\n a letter to number translation(L2N or 2),\n a letter shift(LS or 3),\n or a symbol cipher(SC or 4)?')).lower()
if 'morse' in language or language == '1':
	messIn = (input('what should become MorseCode? ')).lower()
	sendToFile(MorseCode.transTo(messIn))
elif 'l2n' in language or language == '2':
	messIn = (input('what should go into the letter shift? ')).lower()
	sendToFile(LetterNum.transTo(messIn))
elif 'ls' in language or language == '3':
	messIn = (input('what string should be changed into numbers? ')).lower()
	sendToFile(LetterShift.transTo(messIn))
elif 'sc' in language or language == '4':
	messIn = (input('what should become a symbol cipher? ')).lower()
	sendToFile(SymbolCipher.transTo(messIn))






