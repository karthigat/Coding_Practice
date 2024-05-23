# Bubble sort
# It is the simplest and easiest sort algorithm
# It traverse from left to right and swap the elements
# The largest element is moved to rightmost
# Time complexsity
    # Best case - O(n) if it is sorted alreay
    # Worst case - O(n^2) for passing and comparison

list1 = [1,3,2,6,4]

def Bubble_sort(list1):
    '''
        This function takes a list of elements not sorted in order and sort it in ascending order
        
        args: list1 is the list of unsorted elements

        returns: return sorted array in descending order.

    '''
    j = 0
    while j<len(list1):
        for i in range(1, len(list1)-j):
            if list1[i-1] > list1[i]:
                temp = list1[i]
                list1[i] = list1[i-1]
                list1[i-1] = temp
        j = j+1
    return list1
Bubble_sort(list1)