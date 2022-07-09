#QuickSort

def partition(arr,low,high):
    pivot = low
    pos = low
    for i in range(pos+1,high+1):
        if arr[i]<=arr[pivot]:
            pos+=1
            arr[i],arr[pos] = arr[pos],arr[i]
            return pos

def quicksort(arr,low,high):
    if low<high:
        pivot = partition(arr,low,high)
        print("The pivoted number is:",arr[pivot])
        quicksort(arr,low,pivot-1)
        quicksort(arr,pivot+1,high)

arr = [5,4,3,2,1]
quicksort(arr,0,len(arr)-1)
print(f"The Sorted array is: {arr} ")
