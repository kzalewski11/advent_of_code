import math

#read in yer data
infile = open("./input.txt", 'r')

highest_id = 0

#binary space partition calculator
def bsp(string, lowerbound, upperbound):
	#base case is string length 1
	if len(string) == 1:
		if (string == 'F' or string == 'L') :
			return lowerbound
		else:
			return upperbound

	#strip off first character and determine bounds
	param = string[0]
	midpoint = int((upperbound - lowerbound) / 2) + lowerbound

	#F means lower half, B means upper half
	if (param == 'F' or param == 'L'):
		newlower = lowerbound
		newupper = midpoint
	else:
		newlower = midpoint + 1
		newupper = upperbound

	#R E C U R S I O N
	return bsp(string[1:], newlower, newupper)
	
for boarding_pass in infile:
	#get the row
	row = bsp(boarding_pass[0:7], 0, 127)

	#get the column
	column = bsp(boarding_pass[7:], 0, 7)

	#calculate the seat ID
	seat_id = (row * 8 + column)

	#check against the current highest seat ID
	if seat_id > highest_id:
		highest_id = seat_id

infile.close()
print("The highest seat id is", highest_id)
