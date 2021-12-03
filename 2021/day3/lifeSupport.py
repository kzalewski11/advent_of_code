diagFile = open("input.txt")
diagnostics = diagFile.read().splitlines()

gammaRate = ""
epsilonRate = ""

generatorDigits = ""
scrubberDigits = ""

generatorList = diagnostics.copy()
scrubberList = diagnostics.copy()

while len(generatorList) > 1:
	for x in range(0, len(generatorList[0])):
				zeroCount = 0
				oneCount = 0
				for y in range(0, len(generatorList)):
						if int(generatorList[y][x]) == 0:
							zeroCount += 1
						else:
							oneCount += 1

				if oneCount >= zeroCount:
						generatorDigits += str(1)
				else:
						generatorDigits += str(0)

				for diagnostic in list(generatorList):
					if diagnostic[len(generatorDigits) - 1] != generatorDigits[len(generatorDigits) - 1]:
						generatorList.remove(diagnostic)

oxygenGeneratorRating = int(generatorList[0], 2) 

while len(scrubberList) > 1:
	for x in range(0, len(scrubberList[0])):
				zeroCount = 0
				oneCount = 0
				for y in range(0, len(scrubberList)):
						if int(scrubberList[y][x]) == 0:
							zeroCount += 1
						else:
							oneCount += 1

				if oneCount < zeroCount:
						scrubberDigits += str(1)
				else:
						scrubberDigits += str(0)

				for diagnostic in list(scrubberList):
					if diagnostic[len(scrubberDigits) - 1] != scrubberDigits[len(scrubberDigits) - 1]:
						if len(scrubberList) > 1:
							scrubberList.remove(diagnostic)

co2ScrubberRating = int(scrubberList[0], 2)
lifeSupportRating = oxygenGeneratorRating * co2ScrubberRating

print("The life support rating is " + str(lifeSupportRating))
