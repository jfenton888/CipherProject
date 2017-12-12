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
			for b in range(len(inMessage)):
				outMessage[b] = self.diction(b)

		def diction(i):
			corespond = [[' abcdefghijklmnopqrstuvwxyz0123456789'],[' ', '•– ', '–••• ', '–•–• ', '–•• ', '• ', '••–• ', '––• ', '•••• ', '•• ', '•––– ', '–•– ', '•–•• ', '–– ', '–• ', '––– ', '•––• ', '––•– ', '•–• ', '••• ', '– ', '••– ', '•••– ', '•–– ', '–••– ', '–•–– ', '––•• ', '––––– ', '•–––– ', '••––– ', '•••–– ', '••••– ', '••••• ', '–•••• ', '––••• ', '–––•• ', '––––• ', '']]
			return corespond[1][corespond[0][0].find(word[i])]

		def diction2(b):
			corespond2 = [[' ', '•– ', '–••• ', '–•–• ', '–•• ', '• ', '••–• ', '––• ', '•••• ', '•• ', '•––– ', '–•– ', '•–•• ', '–– ', '–• ', '––– ', '•––• ', '––•– ', '•–• ', '••• ', '– ', '••– ', '•••– ', '•–– ', '–••– ', '–•–– ', '––•• ', '––––– ', '•–––– ', '••––– ', '•••–– ', '••••– ', '••••• ', '–•••• ', '––••• ', '–––•• ', '––––• ', ''], [' abcdefghijklmnopqrstuvwxyz0123456789']]
			return corespond2[1][corespond2[0][0].find(word[b])]

	class LetterNum(inMessage):
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
			for b in range(len(inMessage)):
				outMessage[b] = self.diction(b)

		def diction(i):
			corespond = [['abcdefghijklmnopqrstuvwxyz0123456789'],['1','2','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36']]
			return corespond[1][corespond[0][0].find(word[i])]

		def diction2(b):
			corespond2 = [['1','2','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36'], ['abcdefghijklmnopqrstuvwxyz0123456789']]
			return corespond2[1][corespond2[0][0].find(word[b])]


	class LetterShift(inMessage):
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
			for b in range(len(inMessage)):
				outMessage[b] = self.diction(b)

		def diction(i):
			corespond = [['abcdefghijklmnopqrstuvwxyz0123456789'],['BCDEFGHIJKLMNOPQRSTUVWXYZ0123456789A']]
			return corespond[1][corespond[0][0].find(word[i])]

		def diction2(b):
			corespond2 = [['BCDEFGHIJKLMNOPQRSTUVWXYZ0123456789A'],['abcdefghijklmnopqrstuvwxyz0123456789']]
			return corespond2[1][corespond2[0][0].find(word[b])]



'''
cipher = Cipher()
morse = Cipher.MorseCode
morse.
	#letters changed

'''
	#symbols

