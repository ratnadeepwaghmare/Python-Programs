#PS: Count of Even and Odd numbers in given string
x = input("Enter String==>")
new_list = ""
even_count = 0
odd_count = 0
for v in x:
    if v.isdigit():
        if int(v)%2 == 0:
            even_count +=1
        else:
            odd_count +=1

print("Count of Even Numbers is==>",even_count)
print("Count of Odd Numbers is==>",odd_count)