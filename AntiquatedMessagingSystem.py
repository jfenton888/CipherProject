# class Cipher(inMessage, inLanguage):
	
# 	def __init__(self, chooseLanguage):
# 		self.chooseLanguage = inLanguage

class MorseCode:
	"""docstring for MorseCode"""

	def __init__(self):
		self.diction = [[' abcdefghijklmnopqrstuvwxyz0123456789'],[' ', '•– ', '–••• ', '–•–• ', '–•• ', '• ', '••–• ', '––• ', '•••• ', '•• ', '•––– ', '–•– ', '•–•• ', '–– ', '–• ', '––– ', '•––• ', '––•– ', '•–• ', '••• ', '– ', '••– ', '•••– ', '•–– ', '–••– ', '–•–– ', '––•• ', '––––– ', '•–––– ', '••––– ', '•••–– ', '••••– ', '••••• ', '–•••• ', '––••• ', '–––•• ', '––––• ', '']]
		self.outMessage = []

	def transTo(self, inMessage):

		for i in range(len(inMessage)):
			# print(i)
			# print(len(inMessage))
			# print(inMessage[i])
			#print(self.diction[0][0].find(inMessage[i]))
			# print(self.diction[1][self.diction[0][0].find(inMessage[i])])
			# print(self.diction[1][0])
			code = (self.diction[1][self.diction[0][0].find(inMessage[i])])
			(self.outMessage).append(code)
		return MorseCode.send()


	def send(self):
		message = ''.join(self.outMessage)
		return message

	# def diction(self):

		
	# 	corespond = [[' abcdefghijklmnopqrstuvwxyz0123456789'],[' ', '•– ', '–••• ', '–•–• ', '–•• ', '• ', '••–• ', '––• ', '•••• ', '•• ', '•––– ', '–•– ', '•–•• ', '–– ', '–• ', '––– ', '•––• ', '––•– ', '•–• ', '••• ', '– ', '••– ', '•••– ', '•–– ', '–••– ', '–•–– ', '––•• ', '––––– ', '•–––– ', '••––– ', '•••–– ', '••••– ', '••••• ', '–•••• ', '––••• ', '–––•• ', '––––• ', '']]
	# 	return 

#letters changed


#symbols

MorseCode = MorseCode()


messIn = input('what should become MorseCode? ')
print(MorseCode.transTo(messIn))