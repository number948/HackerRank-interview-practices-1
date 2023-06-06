def flippingMatrix(matrix):
  print(matrix)
  diagonal = 0
  suma = 0
  matrix[2].reverse()

  '''fila_temporal = matrix.pop(0)
  
  fila_temporal_1 = matrix.pop(2)
  fila_temporal_2 = matrix.pop(1)

  matrix.insert(3, fila_temporal)
  matrix.insert(0, fila_temporal_1)
  matrix.insert(1, fila_temporal_2)'''
  for i in range(len(matrix)):
        for j in range(len(matrix)):
             if i == j:
                diagonal+= matrix[i][j]
        
  ultima = matrix[3]
  
  for i in ultima:
     suma+= i
  
  print(suma)

 



matrix = [[112, 42, 83, 119], 
         [56, 125, 56, 49],
         [15, 78, 101, 43],
         [62, 98, 114, 108]]

flippingMatrix(matrix)