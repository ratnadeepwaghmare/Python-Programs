#PS: wap to count the occurrences of words in given string

#Solution no.1
str_1 = input("Enter String==>")
pos = 0
for i in str_1.split():
    if i in str_1 and i not in str_1.split()[pos+1:]:
        print("Count of ", i, "is:", str_1.split().count(i))
    pos += 1
    

# Solution no.2

list_1 = list(input("Enter String==>").split())
list_2 = list_1.copy()
count_1 = 0
for i in list_1:
    j = len(list_2)
    while j!=0:
        if i == list_2[j-1] and i!=None:
            count_1+=1
            list_2[j-1] = None
            list_1[j-1] = None
        j-=1
    if i!=None:
        print("Count of ", i, " is :", count_1)
        count_1 = 0
