#PS: Remove the characters which have odd index
x = input("Enter String==>")
new_list = ""
for i,v in enumerate(x):
    if i%2==0:
        new_list +=v
print("original list==",tuple(enumerate(x)))
print("New List after Deleted odd Index Character is ==>",new_list)