# Quick sort

def Partition(partition_list, low, high):
    print('enter')
    print(partition_list)
    i = low - 1
    j=0
    pivot = partition_list[high]
    print(pivot)
    while j <= len(partition_list)-1:
        if pivot >= partition_list[j]:
            i = i+1
            print(i)
            temp = partition_list[i]
            partition_list[i] = partition_list[j]
            partition_list[j] = temp
        j = j+1
    return i, partition_list


def Quick_sort(list1, low, high):

    if len(list1) < 1: 
        return 
    i_value = Partition(list1, low, high)
   
    print('i_value', i_value)
    Quick_sort(list1, low, i_value-1)
    print('working1')
    Quick_sort(list1, i_value+1,high)
    print('working2')

def Start():
    list1 = [1,4,3,8,5,2,7,6]
    low = 0
    Quick_sort(list1, low, len(list1)-1)
    return list1

print(Start())