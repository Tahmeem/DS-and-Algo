def merge_sort(arr):
	merge_sort2(arr,0,len(arr)-1)


def merge_sort2(arr,first,last):
	if first < last: #theres more than 1 item in arr
		middle = (first+last)//2
		merge_sort2(arr,first,middle)
		merge_sort2(arr,middle+1,last)
		merge(arr,first,middle,last)

def merge(arr,first,middle,last):
	l = arr[first:middle]
	R = arr[middle:last+1]
	l.append(9999999)
	R.append(9999999)
	i = j = 0
	for k in range(first,last+1):
		if l[i] <= R[j]:
			arr[k] = l[i]
			i+= 1 
		else:
			arr[k] = R[j]
			j+= 1 