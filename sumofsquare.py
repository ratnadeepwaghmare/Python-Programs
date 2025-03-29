#PS: Find a Sum of Square of first n numbers
from functools import reduce
x = int(input("Enter a Number at which Sum of Square to be Find ==>"))
print("Square of first ",x," Number:",list(map((lambda i:i*i),range(1,x+1))))
sum = reduce((lambda i,j:i+j),(map((lambda i:i*i),range(1,x+1))))
print("Sum of all Squares is==>",sum)