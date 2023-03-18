def minMaxSum(arr):
    copia_arr = arr.copy()
    min_num = arr[0]
    max_num = arr[0]
    sum_min = 0
    sum_max = 0
   
    for i in copia_arr:
        if i > max_num:
            max_num = i
    print(max_num)

    copia_arr.remove(max_num)

    for  i in range(len(copia_arr)):
        sum_min += copia_arr[i]

    for i in arr:
        if i < min_num:
            min_num = i
    #print(min_num)

    arr.remove(min_num)
    #print(arr)

    for i in range(len(arr)):
        sum_max += arr[i]
        
                

    print(sum_min,sum_max)

minMaxSum([7, 69, 2, 221, 8974])