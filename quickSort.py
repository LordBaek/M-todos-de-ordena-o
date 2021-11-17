def partition(arr, low, high):
    i = (low-1) # index of smaller element
    pivot = arr[high] # pivot is the last element of the array

    for j in range(low, high): # loop through the array
        if arr[j] <= pivot: # if the element is smaller than the pivot
            i = i+1 # increment the index
            arr[i], arr[j] = arr[j], arr[i] # swap the elements

    arr[i+1], arr[high] = arr[high], arr[i+1] # swap the pivot with the last element smaller than the pivot
    return (i+1) # return the index of the pivot

def quickSort(arr, low, high): # quick sort algorithm
    if len(arr) == 1: # if the array has only one element
        return arr # return the array

    if low < high: # else if the low index is smaller than the high index
        pi = partition(arr, low, high) # partition the array
        quickSort(arr, low, pi-1) # sort the left part of the array
        quickSort(arr, pi+1, high) # sort the right part of the array



arr = [10, 7, 8, 9, 1, 5] # unsorted array
n = len(arr) # length of the array
quickSort(arr, 0, n-1) # sort the array, the low and high values come from here and are passed to the partition function
print(f"Sorted array is: {arr}") # print the sorted array
