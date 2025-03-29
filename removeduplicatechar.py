#PS: remove duplicate characters in given string
x = input("Enter String==>")
temp = x[:]
new_str = ""
for i,v in enumerate(temp):
    if v in temp[i+1:]:
        pass
    else:
        new_str +=v
print("New String Without Duplicate Characters==>",new_str)