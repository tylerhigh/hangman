import random

def main():


	play = True
	while play:
		words = ["classroom", "desk", "table", "computer", "tower",
				 "picture", "hangman", "disc", "disk", "testing", "this",
				 "movie", "dicing", "rocking", "random", "shirt", "helping",
				 "mother", "father", "sister", "brother", "tie", "fan",
				 "button", "power", "users", "program", "coding", "within",
				 "shoelace", "shoe", "glasses", "name", "tray", "food", "steak",
				 "porkchop", "hive", "standing", "mouse", "scrolling", "with"]
		chosen = random.choice(words)
		guess = None
		letters = []
		word = []
		for letter in chosen:
			word.append("_")
		joined = None

		hangman = (

''' 
_______
|     |
|
|
|
|______
|     |
''', 
'''
_______
|     |
|     O
|
|
|______
|     |
''',
'''
_______
|     |
|    _O
|    
|
|______
|     |
''',
'''
_______
|     |
|    _O_
|
|
|______
|     |
''',
'''
_______
|     |
|    _O_
|     |   
|
|______
|     |
''',
'''
_______
|     |
|    _O_
|   / |
|
|______
|     |
''',
'''
_______
|     |
|    _O_
|   / | \\
|
|______
|     |
''',
'''
_______
|     |
|    _O_
|   / | \\
|    /
|______
|     |
''',
'''
_______
|     |
|    _O_
|   / | \\
|    / \\
|______
|     |

''')

		print(hangman[0])
		attempt = len(hangman) - 1

		while (attempt != 0 and "_" in word):
			print(("Attempts remaning: {}").format(attempt))
			joined = "".join(word)
			print(joined)

			try:
				guess = str(input("Type a letter: "))
			except:
				print("You entered something invalid, try again.")
			else:
				if not guess.isalpha():
					print("You entered something invalid, try again.")
					continue
				elif len(guess) > 1:
					print("Only one letter please.")
					continue
				elif guess in letters:
					print("Already guessed that letter, try again.")
					continue
				else:
					pass

			letters.append(guess)

			for letter in range(len(chosen)):
				if guess == chosen[letter]:
					word[letter] = guess

			if guess not in chosen:
				attempt -= 1
				print(hangman[(len(hangman) - 1 ) - attempt])

		if "_" not in word:
			print(("You win! The word was {}.").format(chosen))
		else:
			print(("You lose! The word was {}.").format(chosen))


		response = input("Do you want to play again?: ").lower()
		if response not in ("yes", "Yes", "y", "Y", "si"):
			play = False

if __name__ == "__main__":
	main()				  