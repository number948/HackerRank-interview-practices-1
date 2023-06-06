def flippingMatrix(matrix):
   
   #invertir la columna 83,56,101,114
   suma = 0
   indice_columna = 2
   for i in range(len(matrix)//2):
        matrix[i][indice_columna], matrix[-i-1][indice_columna] = matrix[-i-1][indice_columna], matrix[i][indice_columna]
   
   #invertir fila 
   matrix[0].reverse()

   #obtener los cuatro numeros upper-left de la matriz
   upper_left_quadrant =  matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1] 
  
   #suma numeros imprimir la suma
   ultima = upper_left_quadrant
   
   for i in ultima:
      suma+= i
   print(suma)


matrix = ([[112, 42, 83, 119], 
           [56, 125, 56, 49],
           [15, 78, 101, 43],
           [62, 98, 114, 108]])

flippingMatrix(matrix)