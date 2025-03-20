#PS: wap to remove the nth index character from non-empty string

str_1 = input("Enter String==>")
index_1 = int(input("Enter Index at which Character to be Delete==>"))
new_str =""
for i,v in enumerate(str_1):
    if i == index_1:
        del i
        print("Deleted Character==>",v)
    else:
        new_str +=v
print("Original String( Index , Value )==>",list(enumerate(str_1)))
print("New String==>",new_str)

