star = "*"

# Functions to display horizontal and vertical stars
def print_horiz_stars(num_stars):
  print num_stars * star
def print_vert_stars(num_stars):
   num = 1
   while num <= 5:
     print star
     num = num + 1

# printing E using stars
print_horiz_stars(10)
print_vert_stars(5)
print_horiz_stars(8)
print_vert_stars(5)
print_horiz_stars(10)
