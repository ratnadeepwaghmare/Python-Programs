#PS: Given string contains all digits only
flag1 = 0
x = input("Enter String==>")
for v in x:
    if v.isdigit():
        pass
    else:
        print("It Contains First Character==>",v)
        flag1 = 1
        break
if flag1 == 0:
    print("It Contains All Digits ==>",x)