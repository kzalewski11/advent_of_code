import re

#read in yer data
infile = open("./input.txt", 'r')
batch = infile.read()

#split each passport out
passports = batch.split('\n\n')

#counter for valid passports
valid = 0
print("There are", len(passports), "passports in the set.")

#set of required keys
reqs = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

for passport in passports:
	#split the passport into fields by one or two spaces
	fields = re.split(r'\s', passport)
	keys = set()
	#split off the key from each field and add to set of keys for passport
	for field in fields:
		key = field.split(':')[0]
		keys.add(key)
	
	#compare set of keys against requirements
	if reqs.issubset(keys):
		valid += 1

print(valid, "are valid.")
