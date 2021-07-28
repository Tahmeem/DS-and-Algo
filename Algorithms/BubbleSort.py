arr = [64,34,25,12,22,11,90]

swap = False
while not swap:
	swap = True
	for i in range(len(arr)-1):
		if arr[i] > arr[i+1]:
			swap = False
			arr[i],arr[i+1] = arr[i+1],arr[i]
print(arr)

#T O(n^2) S O(1)