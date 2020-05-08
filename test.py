# test code for students

# we want to see if our quicksort function works

from school_content import student, QuickSort 

# code 

def partition(collection, low, high):
    # high = len-1
    j = low # collection[j] and every element before it is < pivot
    pivot = high

    for i in range(low, high):
        if (collection[i] < collection[pivot]):
            collection[i], collection[j] = collection[j], collection[i] 
            j += 1
    collection[pivot], collection[j] = collection[j], collection[pivot]
    return j 
    
def quicksort(collection, low, high):
    # high = len-1
    if (low < high):
        pivot = partition(collection, low, high)
        quicksort(collection, low, pivot-1)
        quicksort(collection, pivot+1, high) 


newlist = [0, 9, 3, 7, 6, 1, 8, 2, 5, 4] # list to test our algorithm on 
n = len(newlist)

quicksort(newlist, 0, n-1) 

print(newlist)  