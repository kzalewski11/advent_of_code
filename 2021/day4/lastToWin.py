inputText = open("input.txt")

calledNumbers = [int(num) for num in inputText.readline().split(",")]

#discard newline
inputText.readline()

rowsList = inputText.readlines()
rowNumsList = []
cardsList = []
winningCards = []
winningNumbers = []

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

origNum = len(cardsList)

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

def check_set_pair(pair, num):
	if pair[0] == num:
		pair[1] = True

def mark_card(card, num):
	for row in card:
		for pair in row:
			check_set_pair(pair, num)
	
def pretty_print(card):
	cardString = "\n"
	for row in card:
		for elem in row:
			if elem[1] == True:
				cardString += "(" + str(elem[0]) + ")"
			else:
				cardString += " " + str(elem[0]) + " "
			if elem[0] < 10:
				cardString += " "
		cardString += "\n"
	return cardString

def call_numbers(numbers):
	for num in numbers:
		remainingCards = cardsList.copy()
		for card in remainingCards:
			mark_card(card, num)
			if check_card(card):
				winningCards.append(card)				
				winningNumbers.append(num)
				cardsList.remove(card)
		if len(cardsList) == 0:
			return

def find_sum_unmarked(card):
	total = 0
	for row in card:
		for pair in row:
			if pair[1] == False:
				total += pair[0]
	return total

call_numbers(calledNumbers)

lastWinningCard = winningCards[len(winningCards)-1]
lastWinningNumber = winningNumbers[len(winningNumbers)-1]

finalScore = lastWinningNumber * find_sum_unmarked(lastWinningCard)
print("Your final score with this card is " + str(finalScore))
