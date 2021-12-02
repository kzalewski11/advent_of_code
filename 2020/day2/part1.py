passwords = open("./input.txt", )
count = 0;

for line in passwords:
	bounds = line.rsplit(' ')[0]
	letter = line.rsplit(' ')[1][0]
	password = line.rsplit(' ') [2]

	lowerbound = bounds.rsplit('-')[0]
	upperbound = bounds.rsplit('-')[1]

	if (int(lowerbound) <= password.count(letter) and int(upperbound) >= password.count(letter)):
		count += 1

print(count)

	

	
