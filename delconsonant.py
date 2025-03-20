#PS: wap Make new string with all consonant deleted from the following string
str_1 ="Hello,have a good day"
count_c = ""
count_v = ""
count_s = ""
count_d = ""
for x in str_1:
    if any(c in "@#$%^&*()-+?_=,<>/" for c in x):
        count_s = count_s+x
    elif x=="a" or x=="e" or x=="i" or x=="o" or x=="u"\
            or x=="A" or x=="E" or x=="I" or x=="O" or x=="U":
        count_v = count_v+x
    elif x.isdigit()==1:
        count_d = count_d+x
    elif x == " ":
        pass
    else:
        count_c = count_c+x

print("String of Consonant Character==>",count_c,"\nString of Vowels Character==>",count_v)
print("String of Special Characters==>",count_s,"\nString of Numeric Value==>",count_d)