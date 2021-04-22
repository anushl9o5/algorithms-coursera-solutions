
def count_split(array, counter):
    
    if len(array) == 1:
        return array, counter
        
    if len(array) == 2:
        if array[0] > array[1]:
            return [array[1], array[0]], counter+1
        else:
            return array, counter
            
    a, num_a = count_split(array[:len(array)//2], counter)
    b, num_b = count_split(array[len(array)//2:], counter)
    i, j = 0, 0
    c = []
    
    while(1):
        if a[i] > b[j]:
            counter = counter + (len(a) - i)
            c.append(b[j])
            j+=1
        else:
            c.append(a[i])
            i+=1
            
        if i >= len(a):
            break
        if j >= len(b):
            break

    if (i >= len(a)):
        c+=b[j:]
    elif(j>=len(b)):
        c+=a[i:]
        
    return c, counter+num_a+num_b

if __name__ =="__main__":

    with open('array.txt', 'r') as f:
        num_list = [int(i) for i in f.readlines()]
    
    print(len(num_list))
    print(count_split(num_list, 0)[1])
    
