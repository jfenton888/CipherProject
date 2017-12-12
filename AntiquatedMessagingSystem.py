


def sendToFile(encodedMessage):
	f = open('helloworld.txt','a')
	f.write(encodedMessage)
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
		self.diction = [[' abcdefghijklmnopqrstuvwxyz0123456789'],['1','2','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36']]
		self.outMessage = []

	def transTo(self, inMessage):

		for i in range(len(inMessage)):
			code = (self.diction[1][self.diction[0][0].find(inMessage[i])])
			(self.outMessage).append(code)
		return MorseCode.send()

	def send(self):
		message = ''.join(self.outMessage)
		return message


class LetterShift:
		def __init__(self):
		self.diction = [[' abcdefghijklmnopqrstuvwxyz0123456789'],['BCDEFGHIJKLMNOPQRSTUVWXYZ0123456789A']]
		self.outMessage = []

	def transTo(self, inMessage):

		for i in range(len(inMessage)):
			code = (self.diction[1][self.diction[0][0].find(inMessage[i])])
			(self.outMessage).append(code)
		return MorseCode.send()

	def send(self):
		message = ''.join(self.outMessage)
		return message


MorseCode = MorseCode()
LetterNum = LetterNum()
LetterShift = LetterShift()
language = '0' 

while (('morse' not in language) and ('l2n' not in language) and ('ls' not in language) and ('sc' not in language)):
	language = (input('What code language do you want your message changed into? \n Morse Code(Morse), a letter to number translation(L2N), a letter shift(LS), or a symbol cipher(SC)?')).lower
if 'morse' in language:
	messIn = (input('what should become MorseCode? ')).lower
	MorseCode.transTo(messIn))
elif 'l2n' in language:
	messIn = (input('what should become go into the letter shift? ')).lower
	LetterNum.transTo(messIn))
elif 'ls' in language:
	messIn = (input('what should become numbers? ')).lower 
	LetterShift.transTo(messIn))
elif 'sc' in language:
	messIn = (input('what should become a symbol cipher? ')).lower
	SymbolCiph.transTo(messIn))





