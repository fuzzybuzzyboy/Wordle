import random

Max = 6
Result = ""

Words = open('Words.txt').read().splitlines()
Random_Word = random.choice(Words)
Random_Word = Random_Word.upper()

# print(f"Word is : '{Random_Word.lower()}'\n{Random_Word[0]}, {Random_Word[1]}, {Random_Word[2]}, {Random_Word[3]}, {Random_Word[4]}\n") # only if u want to cheat the game

print("Welcome to wordle.\n🟩 = Correct, 🟧 = Wrong spot, correct letter, 🟥 = Wrong.\n")

while True:
	Word_input = input("Input a five letter word : ")
	NumberCheck = any(chr.isdigit() for chr in Word_input)
	if NumberCheck == True:
		print("Word contains numbers, try again")
		continue
	else:
		Word_input = Word_input.upper()

		if len(Word_input) != 5:
			print("Invaild, please use five letter words")
			continue

	Result=""
	Max -= 1
	for i in range(5):
		if Word_input[i]==Random_Word[i]:
			Result=Result+"🟩"
		else:
			#print(Random_Word.find(Word_input[i]))
			if Random_Word.find(Word_input[i])>-1:
				Result=Result+"🟧"
			else:
				Result=Result+"🟥"
	if Result == "🟩🟩🟩🟩🟩":
		exit(f'{Result}\nYou won :D')
	elif Max == 0:
		exit(f'\n{Result}\nYou lost. The word was : {Random_Word.lower()}')
	else:
		print(Result)
