
'''
Write a function that produces the following output using for-loop:
1 4 9 16 25 36 49 64 81 100


'''

class LoopSquares:
	def loopSquares(self):
		i = 1;
		inc = 3;
		z = 0;
		for j in range(0, int(100/10)):
			print (i, end=' ');
			i = i + inc + j + z;
			z = z + 1;
l = LoopSquares()
l.loopSquares()




