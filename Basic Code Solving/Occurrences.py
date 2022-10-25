


sample = "10,10,20,30,10,30,40"

def counts(string, target):
	count = 0;
	for each in sample:
		if (each != ','):
			if (int(each) == target):
				count = count + 1;
	return count;

print (counts(sample, 9))




