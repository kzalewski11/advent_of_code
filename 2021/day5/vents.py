inputText = open("input.txt")
lines = inputText.read().split("\n")
linesList = []
horVertOnlyList = []

# make a list of ordered pairs (of ordered pairs)
for textLine in lines:
	line = []
	if textLine == '':
		break
	points = textLine.split(" -> ")
	for point in points:
		strPair = point.split(",")
		intPair = list(map(int, strPair))
		line.append(intPair)
	linesList.append(line)

# pick out all vertical/horizontal lines
for line in linesList:
	if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
		horVertOnlyList.append(line)

# get all points that need plotted
allPoints = []
for line in horVertOnlyList:
	if line[0][0] == line[1][0]:
		if line[0][1] < line[1][1]:
			for x in range(line[0][1], line[1][1] + 1):
				allPoints.append([line[1][0], x])
		else:
			for x in range(line[1][1], line[0][1] + 1):
				allPoints.append([line[1][0], x])
			
	if line[0][1] == line[1][1]:
		if line[0][0] < line[1][0]:
			for x in range(line[0][0], line[1][0] + 1):
				allPoints.append([x, line[0][1]])
		else:
			for x in range(line[1][0], line[0][0] + 1):
				allPoints.append([x, line[0][1]])
			
plane = [ [0] * 1000 for _ in range(1000)]


def fill_plane(plane, points):
	for pair in points:
		x = pair[0]
		y = pair[1]
		plane[x][y] += 1

fill_plane(plane, allPoints)

total = 0
for line in plane:
	for num in line:
		if num > 1:
			total += 1
		
print(total)
