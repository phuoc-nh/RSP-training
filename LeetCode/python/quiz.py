# Enter an odd positive integer: 5
# The diamond pattern is:
#   *
#  ***
# *****
#  ***
#   *

number = int(input("Enter an odd positive integer: "))
print("The diamond pattern is:")

for i in range(number):
  numberOfSpace = (abs(i * 2 + 1 - number) // 2)
  print(" " * numberOfSpace, end="") 
  print("*" * (number - numberOfSpace * 2), end="")
  print(" " * numberOfSpace)