moveList = open("input.txt")
moves = moveList.read().splitlines()

parsedList = []
for x in moves:
	dir = x.split(" ")[0]
	mag = x.split(" ")[1]
	x = (dir, int(mag))
	parsedList.append(x)

horizontalPosition = 0
depth = 0

for x in parsedList:
	dir = x[0]
	mag = x[1]
	if dir == 'down':
		depth += mag
	elif dir == 'up':
		depth -= mag
	else:
		horizontalPosition += mag

answer = horizontalPosition * depth
print("The answer is " + str(answer))
