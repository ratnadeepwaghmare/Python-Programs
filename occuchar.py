#PS: wap to count the occurrences of characters in given string

list_1 = list(input("Enter String==>"))
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