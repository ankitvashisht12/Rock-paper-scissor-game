from random import randint
import time

player = input('which one you choose rock(r) , paper(p) or scissor(s)\t')

print('Loading....Computer is thinking')
time.sleep(2)

computer = randint(1,3)


if computer == 1:
	AI = 'r'
elif computer == 2:
	AI = 'p'
else:
	AI = 's'

print('Computer has choosen ' + AI + '\n')

if player == AI:
	print('###  Draw  #### \n Try Luck next time')
elif player == 'r' and AI == 's':
	print('You wins')
elif player == 'r' and AI == 'p':
	print('Computer wins')
elif player == 'p' and AI == 'r':
	print('You wins')
elif player == 'p' and AI == 's':
	print('Computer wins')
elif player == 's' and AI == 'r':
	print('Computer wins')
elif player == 's' and AI == 'p':
	print('You wins')
else:
	print('You entered wrong input !!!')






