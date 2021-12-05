inputText = open("input.txt")

calledNumbers = [int(num) for num in inputText.readline().split(",")]

#discard newline
inputText.readline()

rowsList = inputText.readlines()
rowNumsList = []
cardsList = []

for row in rowsList:
	if row != "\n":
		rowNums = [[int(num), False] for num in filter(None, row.split(" "))]
	else:
		rowNums = row
	rowNumsList.append(rowNums)

#in bird culture, the following line is considered a "dick move"
rowNumsList.append("\n")

card = []
for row in rowNumsList:
	if row != "\n":
		card.append(row)
	else:
		cardsList.append(card)
		card = []

def check_row(card, row):
	for number in card[row]:
		if number[1] == False:
			return False
	return True

def check_column(card, column):
	for row in card:
		if row[column][1] == False:
			return False
	return True

def check_card(card):
	for row in range(0, 5):
		if check_row(card, row):
			return True

	for column in range(0, 5):
		if check_column(card, column):
			return True
	return False

def call_numbers(numbers):
	for num in numbers:
		for card in cardsList:
			for row in card:
				for pair in row:
					if pair[0] == num:
						pair[1] = True
						if check_card(card):
							print("Card " + str(card[0][0][0]) + " wins with number " + str(num))
							return card, num

def pretty_print_card(card):
	for row in card:
		for value in row:
			print(value[0])

def find_sum_unmarked(card):
	total = 0
	for row in card:
		for pair in row:
			if pair[1] == False:
				total += pair[0]
	return total

winner, lastNumber = call_numbers(calledNumbers)

finalScore = lastNumber * find_sum_unmarked(winner)
print("Your final score with this card is " + str(finalScore))
