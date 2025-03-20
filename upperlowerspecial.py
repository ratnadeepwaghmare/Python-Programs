#PS: wap to check count of Upper Character,Lower Character,Numeric values and Special Characters in given string
str_1 = input("Enter String==>")
count_u = 0
count_l = 0
count_s = 0
count_d = 0
for x in str_1:
    if any(c in "@#$%^&*()-+?_=,<>/" for c in x):
        count_s+=1
    elif x.lower() == x and x.isdigit()!=1:
        count_l+=1
    elif x.upper() == x and x.isdigit()!=1:
        count_u += 1
    elif x.isdigit()==1:
        count_d += 1
    else:
        pass

print("Count of Upper Character==>",count_u,"\nCount of Lower Character==>",count_l)
print("Count of Special Characters==>",count_s,"\nCount of Numeric Value==>",count_d)