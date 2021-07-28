


def binary_search(arr,item): #arr must be sorted 
	start = 0 
	last = len(arr)-1

	while start <= last:
		middle = start + (last - start)//2 #Index for mid
		midVal = arr[middle]
		if midVal == item:
			return middle
		elif midVal > item:
			last = middle - 1 
		else:
			start = middle + 1 
	return -1

print(binary_search([11, 12, 22, 25, 34, 64, 90],0))		
