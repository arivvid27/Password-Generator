from random import randint

word1 = input('Give me a color > ')
word2 = input('Give me a adjective > ')
word3 = input('Give me a animal or object > ')
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!','@','#','$','%','^','&','*']

def pick(characters):
	combination_numbers = len(numbers)
	combination_symbols = len(symbols)
	saftey_regulation1 = randint(0, combination_numbers - 1)
	saftey_regulation2 = randint(0, combination_symbols - 1) 
	password_char1 = characters[saftey_regulation1]
	password_char2 = characters[saftey_regulation2]
	return password_char1
	return password_char2

print(pick(numbers), word1, pick(symbols), word2, pick(symbols), word3)

