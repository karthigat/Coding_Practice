data = [20,3,4,1,2]

def selection_sort(data):
    """
    args: unsorted array of elements
    return: sorted array of elements
    Compare and store the smallest element. Then swap the smalled element with the i index in ascending order
    """
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
                print(data)
        (data[i], data[min_idx]) = (data[min_idx], data[i])
        print(data)
    return data

#best case - o(n^2)
#worst case - O(n^2)
