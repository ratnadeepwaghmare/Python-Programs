#PS: wap to check count of Digits,Vowels,Consonant,White Spaces and Special Characters in given string
str_1 = input("Enter String==>")
count_d = 0
count_v = 0
count_w = 0
count_c = 0
count_s = 0
for x in str_1:
    if x.isdigit() == 1:
        count_d+=1
    elif x=="a" or x=="e" or x=="i" or x=="o" or x=="u"\
            or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
        count_v+=1
    elif x==" ":
        count_w+=1
    elif any(c in "@#$%^&*()-+?_=,<>/" for c in x):
        count_s += 1
    else:
        count_c+=1

print("Count of Digit==>",count_d,"\nCount of Vowels==>",count_v)
print("Count of White Space==>",count_w,"\nCount of Consonant==>",count_c)
print("Count of Spacial Character==>",count_s)