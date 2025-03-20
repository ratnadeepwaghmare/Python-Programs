#PS: wap to exchange first and last characters of given string

str_1 = input("Enter String==>")
new_str =""
fc =""
new_str_1 = ""

last_index = max(i for i, v in enumerate(str_1))
for i,v in enumerate(str_1):
    if i == 0:
        fc = v
    elif i == last_index:
        new_str += v
    else:
        new_str_1 += v

new_str+=new_str_1+fc
print("Original String==>",str_1)
print("New String==>",new_str)