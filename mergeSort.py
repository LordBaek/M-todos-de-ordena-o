def mergeSort(arr):
    if len(arr) > 1:
        
        # original array is broken in two parts
        # left and right array
        a = len(arr)//2
        l = arr[:a]
        r = arr[a:]
        b = c = d = 0
        mergeSort(l) # sort left
        mergeSort(r) # sort right
        
        while b < len(l) and c < len(r): # merge
            if l[b] < r[c]: # if left is smaller
                arr[d] = l[b] # add to result
                b += 1 # increment left index
            else: # if right is smaller
                arr[d] = r[c] # add to result
                c += 1 # increment right index
            d += 1 # increment result index

        while b < len(l): # if left is not empty
            arr[d] = l[b] # add to result
            b += 1 # increment left index
            d += 1 # increment result index

        while c < len(r): # if right is not empty
            arr[d] = r[c] # add to result
            c += 1 # increment right index
            d += 1 # increment result index

if __name__ == '__main__': # test
    arr = [0,1,3,5,7,9,2,4,6,8] 
    mergeSort(arr) 
    print(f"Sorted array is: {arr}")
 