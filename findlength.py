#PS: wap to Find length of the string "machine learning" with and without using len function

print("String ==> machine learning")
#With len function
print("Length of string==>",len("machine learning"))

#without len function
print("Length of string==>",max(i+1 for i, v in enumerate("machine learning")))
