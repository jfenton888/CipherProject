class Cipher(inMessage, inLanguage):
	
	def __init__(self, chooseLanguage):
		self.chooseLanguage = inLanguage

	class MorseCode(inMessage):
		"""docstring for MorseCode"""


		def __init__(self, arg):
			self.transTo = transTo
			self.transBack = transBack
			self.send = send
			self.diction = diction

		def transTo():
			for i in range(len(inMessage)):
				outMessage[i] = self.diction(i)

		def transBack():

		def send():

		def diction(i):

			
			corespond = [[' abcdefghijklmnopqrstuvwxyz0123456789'],[' ', '•– ', '–••• ', '–•–• ', '–•• ', '• ', '••–• ', '––• ', '•••• ', '•• ', '•––– ', '–•– ', '•–•• ', '–– ', '–• ', '––– ', '•––• ', '––•– ', '•–• ', '••• ', '– ', '••– ', '•••– ', '•–– ', '–••– ', '–•–– ', '––•• ', '––––– ', '•–––– ', '••––– ', '•••–– ', '••••– ', '••••• ', '–•••• ', '––••• ', '–––•• ', '––––• ', '']]
			return corespond[1][corespond[0][0].find(word[i])]

	#letters changed


	#symbols
	class Unicode(inMessage):

		def__init__(self, arg):
			self.transTo = transTo
			self.transBack = transBack
			self.send = send
			self.diction = diction

		def transTo():
			for i in range(len(inMessage)):
				outMessage[i] = self.diction(i)

		def transBack():

		def send():

		def diction(i):


			corespond = [[' abcdefghijklmnopqrstuvwxyz0123456789'],[' ','🖯','🖰','🖱','🖲','🖮','🎮','📱','📶','📞','☎','📟','📠','📀','💾','🖫','✇','🖭','🖳','🖥','🖨','🖧','📷','🎥','🎧','🎤','📢','💽','📹','⊗','⊕','🔱','🔭','⚓','🤖','📺','📡', '']]
			return corespond[1][corespond[0][0].find(word[i])]
