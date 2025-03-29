#PS: reverse a string which have string length with multiple of 5
x = list(input("Enter String==>"))
str_len = len(x)
if str_len%5==0:
    x.reverse()
    str_1 ="".join(map(str,x))
    print("string Length is Multiple of 5 : string lenght is:",str_len,"and Reversed String==>",str_1)
else:
    print("string Length is Not Multiple of 5 : string lenght is:", str_len)