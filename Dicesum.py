


import random as r;
class DiceSum:
    def diceSum(self):
       sum = int(input("Enter your desired sum: "))
   
       d1, d2 = 0,0;
       while(d1+d2 != sum):
           d1 = 1 + r.randint(0,5);
           d2 = 1 + r.randint(0,5);
           print (d1, "and" , d2, "=", (d1+d2));
d = DiceSum()
d.diceSum()









