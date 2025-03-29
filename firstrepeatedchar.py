#PS: First Repeated Character in given string
x = input("Enter String==>")
new_list = ""
flag_1 = 0
for i,v in enumerate(x.split()):
    if v==x.split()[i+1]:
        flag_1 += 1
        print("Second Most Repeated Word is==>",v)
        break
