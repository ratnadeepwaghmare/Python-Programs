#PS: wap to find last 10 characters of given string

list_1 = list(input("Enter String==>"))
list_2 = list_1[-10:]
new_string = ''
for i in list_2:
    new_string += i
print("Last 10 Characters :",new_string)