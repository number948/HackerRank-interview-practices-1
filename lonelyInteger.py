def lonelyInteger(arr):
    
    for i in arr:
        if(arr.count(i)==1):
            return i
            
print(lonelyInteger([1,2,3,4,3,2,1]))
    