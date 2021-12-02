depthList = open("input.txt")
depths = depthList.read().splitlines()

increaseCount = 0

for x in range(1, len(depths) - 2):
	triplet_one = int(depths[x - 1]) + int(depths[x]) + int(depths[x + 1])
	triplet_two = int(depths[x]) + int(depths[x + 1]) + int(depths[x + 2])
	if triplet_two > triplet_one:
		increaseCount += 1

print("Total number of increases is " + str(increaseCount))
