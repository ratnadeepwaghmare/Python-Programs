#PS: swap commas with dots in given string
x = input("Enter String==>")
new_list = ""
for i,v in enumerate(x):
    if v==",":
            new_list += "."
    elif v == ".":
            new_list += ","
    else:
            new_list +=v
print("New String==>",new_list)


