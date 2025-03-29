#PS: reverse a word in given string
x = input("Enter String==>")
temp = []
for i in x.split():
    temp = list(i)
    temp.reverse()
    i = "".join(map(str,temp))
    print(i,end=" ")