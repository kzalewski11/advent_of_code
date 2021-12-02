depthList = open("input.txt")
depths = depthList.read().splitlines()

increaseCount = 0

for x in range(1, len(depths)):
	if int(depths[x]) > int(depths[x - 1]):
		increaseCount += 1

print("Total number of increases is " + str(increaseCount))
