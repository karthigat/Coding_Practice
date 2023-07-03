import numpy as np
class MergeSort(object):
    def __init__(self, A, B, m, n):
        self.list_A = A
        self.list_B = B
        self.list_C = np.zeros(n+m)
        self.m = m
        self.n = n

    def merge_sort(self):
        i=j=k=0
        while i < len(self.list_A) and j< len(self.list_B):
            if self.list_A[i] <= self.list_B[j]:
                self.list_C[k] = self.list_A[i]
                i += 1
            else:
                self.list_C[k] = self.list_B[j]
                j += 1
            k += 1
        
        while i < len(self.list_A):

            self.list_C[k] = self.list_A[i]
            i += 1
            k += 1
        while j < len(self.list_B):
            self.list_C[k] = self.list_B[j]
            j += 1
            k += 1
        return self.list_C
    
if __name__ == "__main__":
    obj = MergeSort([1,3,4,5], [2,4,6,8,10], 4, 5)
    print(obj.merge_sort())

