


corespond = [['abcdefghijklmnopqrstuvwxyz0123456789'],['•– ', '–••• ', '–•–• ', '–•• ', '• ', '••–• ', '––• ', '•••• ', '•• ', '•––– ', '–•– ', '•–•• ', '–– ', '–• ', '––– ', '•––• ', '––•– ', '•–• ', '••• ', '– ', '••– ', '•••– ', '•–– ', '–••– ', '–•–– ', '––•• ', '––––– ', '•–––– ', '••––– ', '•••–– ', '••••– ', '••••• ', '–•••• ', '––••• ', '–––•• ', '––––• ', '']]
#corespond = [['ab'],['c', 'd']]
word = input('your word goes here')
print(len(word))
for i in range(len(word)):
	print(corespond[1][corespond[0][0].find(word[i])])