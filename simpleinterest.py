#PS: Calculate a Simple Interest

p = float(input("Enter a Principal Amount==>"))
r = float(input("Enter a Rate of Interest==>"))
t = float(input("Enter a Time Period in Month==>"))
si = (p * r * t) / 100
print("Total Simple Interest is ==>",round(si,2))