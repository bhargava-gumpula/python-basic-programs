import time

def even(num):
  if (num % 2 == 0):
     return True
  else:
     return False

def odd(num):
  if (num % 2 != 0):
     return True
  else:
     return False

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


def is_letter(letter):
   if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z'):
      return True
   else:
      return False

def is_number(number):
   if number >= '0' and number <= '9':
     return True
   else:
     return False

class employee:
  def __init__(self, name, age):
    print "I am in Init function"
    self.name = name
    self.age = age
  def print_name(self):
    print "employee name:"
    print self.name
  def print_age(self):
     print self.age

def factorial(num):
   num = num
   saved_num = num
   fact = 1
   while num >= 1:
      fact = fact * num
      num = num - 1
   print ("Factorial of numer:%d is %d") % (saved_num, fact)
