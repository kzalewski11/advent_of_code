passwords = open("./input.txt", )
count = 0;

for line in passwords:
	bounds = line.rsplit(' ')[0]
	letter = line.rsplit(' ')[1][0]
	password = line.rsplit(' ') [2]

	loc1 = int(bounds.rsplit('-')[0]) - 1
	loc2 = int(bounds.rsplit('-')[1]) - 1

	if ((password[loc1] == letter and password[loc2] != letter) or (password[loc1] != letter and password[loc2] == letter)):
		count += 1

print(count)

	

	
