import random

wins = 0

def reset():
	global lives
	global number
	lives = 5
	number = random.randint(1, 100)

reset()

def numuse(user):
	if user == number:
		return "You guessed correct! "
		
	elif user > number and user > 1:
		
		return "Too high! "
		
	elif user < number and user < 100:
		return "Too low! "
	
	else:
		return "Not in range"

def check(user):
	if lives <= 5 and lives > 0:
		return numuse(user)
	
	else:
		return "Out of lives"

runs = True
def askreset():
	user = input("Do you want to play again? (Y/n): ")
	if user.islower():
		global runs
		runs = False
		print('Current statics: ')
		print(f'Total wins: {wins}')
		print('Bye! ')
	else:
		reset()

print('Bot think number between 1~100')
print('Find the number')
print('You have 5 lives! ')
print('Guess started! \n')

while runs:
	try:
		know = check(int(input('Enter number: ')))
	except Exception as e:
		print(f'Error: {e}\n')
		continue
	if know == "You guessed correct! ":
		wins += 1
		print(f'{know}\n')
		askreset()
	
	elif know == "Out of lives":
		print(f'{know}\n It was number {number}')
		askreset()
	
	else:
		print(f'Left lives: {lives}')
		lives -= 1
		print(f'{know}\n')