import re

#read in yer data
infile = open("./input.txt", 'r')
batch = infile.read()

#split each passport out
passports = batch.split('\n\n')

#counter for valid passports
valid = 0

#set of required keys
reqs = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

for passport in passports:
	#split the passport into fields by one or two spaces
	fields = re.split(r'\s', passport)
	fieldsDict = dict()
	keys = set()
	#split off the key and value from each field and add to dict
	for field in fields:
		field = field.split(':')
		if len(field) > 1:
			fieldsDict[field[0]] = field[1]
		
		keys.add(field[0])

	#compare set of keys against requirements
	if reqs.issubset(keys):
		#check each field's requirements
		#birth year
		if not (int(fieldsDict["byr"]) <= 2002 and int(fieldsDict["byr"]) >= 1920):
			continue
		#issue year
		if not (int(fieldsDict["iyr"]) <= 2020 and int(fieldsDict["iyr"]) >= 2010):
			continue
		#expiration year
		if not (int(fieldsDict["eyr"]) <= 2030 and int(fieldsDict["eyr"]) >= 2020):
			continue
		#height
		if not re.match(r'^[1][5-8][0-9]cm$|^[1][9][0-3]cm$|^[5][0-9]in$|^[6][0-9]in$|^[7][0-6]in$', fieldsDict["hgt"]):
			continue
		#hair color
		if not re.match(r'^#[0-9a-f]{6}$', fieldsDict["hcl"]):
			continue
		#eye color
		if not re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', fieldsDict["ecl"]):
			continue
		#passport id
		if not re.match(r'^[0-9]{9}$', fieldsDict["pid"]):
			continue
		valid += 1
		
print(valid, "valid passports")
