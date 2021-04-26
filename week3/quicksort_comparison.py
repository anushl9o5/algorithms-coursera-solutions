#!/usr/bin/python
class QuickCompare:
    def __init__(self):
        self.count = 0
        
    def partition(self, a, piv):
        i = 1
        for j in range(1, len(a)):
            if a[j] < piv:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp
                i+=1
        
        temp = a[0]
        a[0] = a[i-1]
        a[i-1] = temp
        
        return a[:i-1], a[i:]
    
    def quicksort(self, array, question):
        if len(array) <= 1:
            return array
    
        mid = len(array)//2 - 1
        
        if question == 2:
            temp = array[0]
            array[0] = array[-1]
            array[-1] = temp
            
        if question == 3:
            if array[mid] < array[-1]:
                if array[mid] > array[0]:
                    temp = array[0]
                    array[0] = array[mid]
                    array[mid] = temp
                    
            if array[-1] < array[0]:
                if array[-1] > array[mid]:
                    temp = array[0]
                    array[0] = array[-1]
                    array[-1] = temp
            
            if array[0] < array[mid]:
                if array[0] > array[-1]:
                    pass

        pivot = array[0]
        
        left, right = self.partition(array, pivot)
        
        self.count += len(right) + len(left)
        
        l = self.quicksort(left, question)
        r = self.quicksort(right, question)
        
        return l+[pivot]+r
    

if __name__ =="__main__":
    
    with open('array.txt', 'r') as f:
        num_list = [int(i) for i in f.readlines()]
    
    obj = QuickCompare()
    
    for i in range(3):
        res = obj.quicksort(num_list, i+1)
        print(res[:10], obj.count)
        obj.count = 0
    
