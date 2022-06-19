import array as arr

def SimpleSum(arr):
	sum=0
	n=len(arr)

	for i  in range(n):
		sum=sum + arr[i]

	return sum 

x=arr.array('i',[1,2,3,4,10,11])
print('sum is:',SimpleSum(x))