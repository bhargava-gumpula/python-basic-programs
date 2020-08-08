def print_matrix(matrix, rows, cols):
   r = 0
   while r < rows:
      string = ""
      c = 0
      while c < cols:
         string = string + str(matrix[r][c]) + " "
         c = c + 1
      print string
      r = r + 1

def add_matrices(A,B,rows,cols):
   r = 0
   C = []
   while r < rows:
      temp = []
      c = 0
      while c < cols:
         temp.append(A[r][c] + B[r][c])
         c = c + 1
      C.append(temp)
      r = r + 1
   return C

#########
A = [
     [1,2],
     [3,4]
    ]

B = [
     [0,1],
     [2,3]
    ]

print "Matrix:A"
print_matrix(A, 2, 2)

print("Matrix:B")
print_matrix(B, 2, 2)     

C = add_matrices(A, B, 2, 2)

print("Matrix:C = A + B")
print_matrix(C, 2, 2)
