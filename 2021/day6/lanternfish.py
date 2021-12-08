inputText = open("input.txt")
inputList = inputText.read().split(",")
lanternFish = list(map(int, inputList))

fishCounts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in lanternFish:
	fishCounts[x] += 1

def pool_after(fishList, days):
	if days == 0:
		return fishList
	newList = spawn(fishList)
	return pool_after(newList, days - 1)
		
def spawn(fishList):
	newSpawns = fishList[0]
	for x in range(0, 8):
		fishList[x] = fishList[x + 1]
	fishList[6] += newSpawns
	fishList[8] = newSpawns
	return fishList
	
def count_fish(pool):
	total = 0
	for x in range(0, len(pool)):
		total += pool[x]
	return total

print(count_fish(pool_after(fishCounts, 256)))
