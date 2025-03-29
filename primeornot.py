#PS: Find Number is Prime or Not

x = int(input("Enter a Number to Find Prime or Not ==>"))
flag_1 = 0
for i in range(1,x):
    if i!=1 and i!=x:
        if x%i==0:
            flag_1 = 1
if flag_1 == 1:
    print("Number: ",x," is Not a Prime Number")
else:
    print("Number: ",x," is a Prime Number")