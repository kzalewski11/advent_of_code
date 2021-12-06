inputText = open("input.txt")
lines = inputText.read().split("\n")
linesList = []
horVertOnlyList = []
diagonalList = []

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

# pick out all diagonals
for line in linesList:
	if abs(line[0][0] - line[1][0]) == abs(line[0][1] - line[1][1]):
		diagonalList.append(line)

# get all points from vert/hor lines that need plotted
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

# get all points from diags that need plotted
for line in diagonalList:
	# go from x1 to x2 and y1 to y2, including endpoints, preserving direction (pos, neg)
	# if ascending x
	startx = line[0][0]
	starty = line[0][1]

	stopx = line[1][0]
	stopy = line[1][1]

	currx = line[0][0]
	curry = line[0][1]
	
	while currx != stopx and curry != stopy:
		allPoints.append([currx, curry])
		if currx < stopx:
			currx += 1
		else:
			currx -= 1
		if curry < stopy:
			curry += 1
		else:
			curry -= 1

	allPoints.append([currx, curry])

plane = [ [0] * 1000 for _ in range(1000)]

def fill_plane(plane, points):
	for pair in points:
		x = pair[0]
		y = pair[1]
		plane[x][y] += 1

def print_plane(plane):
	for row in plane:
		print(row)

def print_points(points):
	for point in points:
		print(point)

#print_points(allPoints)
fill_plane(plane, allPoints)
#print_plane(plane)

total = 0
for line in plane:
	for num in line:
		if num > 1:
			total += 1
		
print(total)
