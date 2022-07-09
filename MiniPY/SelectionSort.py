#SelectionSort

arr=[80,70,60,50,40,30,20,10]
for i in range(len(arr)):
	small=arr[i]
	pos=i
	for j in range(i,len(arr)):
		if arr[j]<small:
			small=arr[j]
			pos=j
	arr[i],arr[pos]=arr[pos],arr[i]
print(*arr)