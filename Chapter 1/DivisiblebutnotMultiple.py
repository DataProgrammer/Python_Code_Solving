

l = []

for i in range(5000, 10001):
	if (i%7 == 0) and (i%5 != 0):
		l.append(i)

print (len(l))
print (l[:10])







