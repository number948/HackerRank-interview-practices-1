def plusMinus(arr):
    ceros= 0
    positivos = 0
    negativos = 0
    n = len(arr)
    
    for i in range(len(arr)):
        if arr[i] == 0:
            ceros +=1
            
        elif arr[i]>0:
            positivos +=1
            
        elif arr[i]<0:
            negativos += 1
           
    x = ceros/n
    y = positivos/n
    z = negativos/n

    print("{:.6f}".format((y)))
    print("{:.6f}".format((z)))
    print("{:.6f}".format((x)))
    

plusMinus([-4, 3,-9, 0, 4, 1])



