
s = ''' Python is an interpreted high-level programming language for general-purpose programming. 
		Created by Guido van Rossum and first released in 1991, Python has a design philosophy that 
		emphasizes code readability, notably using significant whitespace. It provides constructs that 
		enable clear programming on both small and large scales.[27] In July 2018, Van Rossum stepped 
		down as the leader in the language community after 30 years. '''

print (len(s))	# for reference; 445

count = 0;

for each in s:
	count = count + 1;

print (count)