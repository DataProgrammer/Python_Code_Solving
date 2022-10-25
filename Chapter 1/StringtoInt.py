
x = "1234567890"

def convert(string):
	temp = 0;
	for i in range(0,10):
		if (string[0] == x[i]):
			print (int(string));
			temp = 1;
		elif ((i == 9) & (temp == 0)):
			print ("Unable to convert")

			
convert("Hello...")
convert("8923")





