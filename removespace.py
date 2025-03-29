#PS: remove spaces in given string
x = input("Enter String==>")
temp = []
for i in x.split():
    temp = list(i)
    i = "".join(map(str,temp))
    print(i,end="")