import numpy as np

r = 101
i = 1
sum = 0
for i in range(r):
	sum += i

print('sum from 1 to 100. answer= ',sum)

sum_by_np = 0
amin = 1
amax = 101
Array = np.arange(amin , amax , 1)
for i in Array:
	sum_by_np += i
print('sum by numpy from ' , amin , ' to ' , amax - 1 , ' = ' , sum_by_np)	
