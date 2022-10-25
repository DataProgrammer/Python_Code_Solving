

import numpy as np

x = 3

y = np.zeros([x,x])


# aa = y.ravel()
# print (aa)
# print (np.zeros_like(aa))

# for each in y:
# 	for one in range(each.shape[0]):
# 		each[one] =  2//2;
# print (y)




temp = list(y)
result = []

for each in temp:
	print (each)
	for one in range(len(each)):
		result.append(0//1);

temp2 = np.array(result).reshape(y.shape)

for each in temp2:
	each[each.shape[0]//2] = 1
	temp2[each.shape[0]//2] = 1;
print (temp2)
# temp = list(y)
# temp1 = []

# for each in temp:
# 	for one in range(len(each)):
# 		temp1.append(0//2)
# print (np.array(temp1).reshape(y.shape))
# # a = np.array([
#     [0, 2, 0, 0],
#     [0, 2, 0, 0],
#     [3, 0, 0, 0],
#     [2, 0, 1, 0],
# ])
# aa = a.ravel()
# b = np.zeros_like(aa)
# for i, x in enumerate(aa):
#     if x != 0:
#         b[i + 1 : i + 1 + x] = 1
# b = b.reshape(a.shape) 

# print (b)