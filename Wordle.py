import random

Max = 6
Result = ""

Words = open('Words.txt').read().splitlines()
Random_word_picker = random.choice(Words)
Letter0 = Random_word_picker[0]
Letter1 = Random_word_picker[1]
Letter2 = Random_word_picker[2]
Letter3 = Random_word_picker[3]
Letter4 = Random_word_picker[4]
Random_word_picker = Random_word_picker.upper()

print(f"Cheater cheater lemon eater. '{Random_word_picker.lower()}'\n{Letter0}, {Letter1}, {Letter2}, {Letter3}, {Letter4}\n")

print("Welcome to wordle.\n🟩 = Correct, 🟧 = Wrong spot, correct letter, 🟥 = Wrong.\n")

while True:
	Word_input = input("Input a five letter word : ")
	NumberCheck = any(chr.isdigit() for chr in Word_input)
	if NumberCheck == True:
		print("Word contains numbers, try again")
		continue
	else:
		Word_input = Word_input.upper()

		if len(Word_input) > 5 or len(Word_input) < 5:
			print("Invaild, please use five letter words")
			continue

		Max -= 1
			
		if Result == "🟩🟩🟩🟩🟩":
			exit("🟩🟩🟩🟩🟩\nYou won!")
		elif Max == 0:
			exit("🟥🟥🟥🟥🟥\nYou lost :(")
		else:
			pass

		print(Result)
