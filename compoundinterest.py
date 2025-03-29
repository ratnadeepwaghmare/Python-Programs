#PS: Calculate a Compound Interest

p = float(input("Enter a Principal Amount==>"))
r = float(input("Enter a Rate of Interest==>"))
t = float(input("Enter a Time Period in Month==>"))
ci = p * (1 + r/100)**t - p
print("Total Compound Interest is ==>",round(ci,2))
