diagFile = open("input.txt")
diagnostics = diagFile.read().splitlines()

parsedList = []

gammaRate = ""
epsilonRate = ""

for y in range(0, len(diagnostics[0])):
				zeroCount = 0
				oneCount = 0
				for x in range(0, len(diagnostics)):
					if int(diagnostics[x][y]) == 0:
						zeroCount += 1
					else:
						oneCount += 1
				if zeroCount > oneCount:
					gammaRate += str(0)
				else:
					gammaRate += str(1)
		
print("The gamma rate is " + gammaRate)
print("The gamma rate in decimal is " + str(int(gammaRate, 2)))

for x in gammaRate:
	if x == '0':
		epsilonRate += '1'
	else:
		epsilonRate += '0'

print("The epsilon rate is " + epsilonRate)
print("The epsilon rate in decimal is " + str(int(epsilonRate, 2)))

powerConsumption = int(epsilonRate, 2) * int(gammaRate, 2)
print("The power consumption is " + str(powerConsumption))
