data = [2,12,4,5,13]

def insertion_sort(data):
    """
    data: array of elements
    return: return sorted array
    The key is compared to the previous element, if key is smaller than previous element then swap the element
    and key.
    """
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        while j>=0 and key < data[j]:
            data[j+1] = data[j]
            j = j - 1
        data[j+1] = key
    return data


 #Bestcase - O(n)
 #Worstcase - O(n^2)