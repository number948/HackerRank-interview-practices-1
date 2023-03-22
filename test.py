def test(arr):
    suma = 0
    media = 0
    n = len(arr)
    arr.sort()
    #print(arr) # hasta aqui el array está ordenado.
    if n%2 != 0:
        mitad = n//2
        mediana = arr[mitad]
        print("la mediana es: ", mediana)
    elif n%2 == 0:
        for i in range(n):
              suma += i
              media = suma/n
        print("la media es: ",media)
      

test([0,1,2,4,6,5,3])


#el resultado debe ser 333