#PS: wap to convert a given string to all uppercase if it contains at least 2 uppercase characters in first 4 character

list_1 = input("Enter String==>")
list_2 = list(list_1)
list_3 = list_2[:4]
count_1 = 0
new_string = ''
for i in list_3:
    new_string += i

for j in list_3:
    if j.isupper() == True:
        count_1+=1
if count_1>=2:
    new_string = list_1.upper()
    print("Uppercase String :", new_string)
else:
    print("There is no two Uppercase character present in first 4 character of string")

