#PS: wap to check word 'orange' is present in the "This is orange juice"
from sqlparse import split

str_1 = "This is orange juice"
#Solution 1
[print("Orange is present") for x in str_1.split(" ") if x=="orange"]

#Solution 2
[None if x!="orange" else print("Orange is present") for x in str_1.split(" ")]

#Solution 3
if any(c in "orange" for c in str_1):
    print("Orange is present")

