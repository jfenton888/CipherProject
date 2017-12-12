
class caesar: #Caesar class fro caesar cipher
	def __init__(self, n, input1):
		self.n = n #number of times you want to switch
		self.input1 = input1 #input to be decoded or encoded
		self.key = 'abcdefghijklmnopqrstuvwxyz' #cipher key

	def encrypt(self):
	    """Encrypt the string and return the ciphertext"""
	    result = '' #adds letters to result

	    for l in self.input1.lower(): #iterates through letters in input
	        try: #try and except statement
	            i = (self.key.index(l) + self.n) % 26 #assigns a latter a new letter based off the key and number of times you wanted to switch. Example: If you switched 3, all the A would become D
	            result += self.key[i]
	        except ValueError:
	            result += l #if there is an error, just assign it l

	    return result.lower() #returns result in lowercase english form


	def decrypt(self): #decryption class for caesar class
	    """Decrypt the string and return the plaintext"""
	    result = ''

	    for l in self.input1: #Reverse of encrypt class as I am subtracting the switch number rather than adding it.
	        try:
	            i = (self.key.index(l) - self.n) % 26
	            result += self.key[i]
	        except ValueError:
	            result += l

	    return result

	def show_encrypt(self):
		self.encrypted = self.encrypt()
		return self.encrypted
	def show_decrypt(self):
		self.decrypted = self.decrypt()
		return self.decrypted

class morse: #Morse cipher class
	def __init__(self, input2):
		self.input2 = input2 #Input
		#Key for encryption
		self.correspond = [['abcdefghijklmnopqrstuvwxyz0123456789'],['•– ', '–••• ', '–•–• ', '–•• ', '• ', '••–• ', '––• ', '•••• ', '•• ', '•––– ', '–•– ', '•–•• ', '–– ', '–• ', '––– ', '•––• ', '––•– ', '•–• ', '••• ', '– ', '••– ', '•••– ', '•–– ', '–••– ', '–•–– ', '––•• ', '––––– ', '•–––– ', '••––– ', '•••–– ', '••••– ', '••••• ', '–•••• ', '––••• ', '–––•• ', '––––• ', '']]
		#Key for decryption
		self.correspond0 = [['•– ', '–••• ', '–•–• ', '–•• ', '• ', '••–• ', '––• ', '•••• ', '•• ', '•––– ', '–•– ', '•–•• ', '–– ', '–• ', '––– ', '•––• ', '––•– ', '•–• ', '••• ', '– ', '••– ', '•••– ', '•–– ', '–••– ', '–•–– ', '––•• ', '––––– ', '•–––– ', '••––– ', '•••–– ', '••••– ', '••••• ', '–•••• ', '––••• ', '–––•• ', '––––• ', ''], ['abcdefghijklmnopqrstuvwxyz0123456789']]
	def correspond1(self):
		result=''
		#print(len(input2))
		for i in range(len(self.input2)): #for every letter/character in the the input
			
			result += self.correspond[1][self.correspond[0][0].find(self.input2[i])] #add the correspodning morse code symbol to result
		return result
	def correspond2(self):
		result=''
		#print(len(input2))
		for i in range(len(self.input2)):
			
			result += self.correspond0[1][self.correspond0[0][0].find(self.input2[i])]#add the correspodning morse code symbol to result. Just reverse this time. Morse to english.
		return result



#print ('Decrytped: %s' % self.decrypted)
#cipher = caesar(3, "khoor")
#cipher.show_result("khoor", 3)

'''
import random


class substitution:
	
	def __init__(self, plaintext):

	alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
	key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'
	plaintext = "Hey, this is really fun!"


	def makeKey(alphabet):
	   alphabet = list(alphabet)
	   random.shuffle(alphabet)
	   return ''.join(alphabet)

	def encrypt(plaintext, key, alphabet):
	    keyMap = dict(zip(alphabet, key))
	    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)

	def decrypt(cipher, key, alphabet):
	    keyMap = dict(zip(key, alphabet))
	    return ''.join(keyMap.get(c.lower(), c) for c in cipher)

	cipher = encrypt(plaintext, key, alphabet)

	print(plaintext)
	print(cipher)
	print(decrypt(cipher, key, alphabet))

sub = substitution('hello')
sub.makeKey()
sub.encrypt("hello", 'nu.t!iyvxqfl,bcjrodhkaew spzgm', list('abcdefghijklmnopqrstuvwxyz.,!')

	'''

