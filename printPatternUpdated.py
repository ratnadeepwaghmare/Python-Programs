
def pattern_1():
    i = 1
    j = 1
    while i!=6:
        [print(i,end=" ") for j in range(0,i)]
        print("")
        i+=1



def pattern_2():
    i = 1
    j = 1
    while i!=7:
        [print(j,end=" ") for j in range(1,i)]
        print("")
        i+=1



def pattern_3():
    i = 6
    j = 1
    k=1
    while i!=0:
        [print(k,end=" ") for j in range(1,i)]
        print("")
        i-=1
        k+=1

def pattern_4():
    i = 6
    j = 1
    while i!=0:
        [print(5,end=" ") for j in range(1,i)]
        print("")
        i-=1



def pattern_5():
    i = 6
    j = 1
    while i!=0:
        [print(i-1,end=" ") for j in range(1,i)]
        print("")
        i-=1

def pattern_6():
    i = 6
    j = 1
    while i!=1:
        [print(j,end=" ") for j in range(0,i)]
        print("")
        i-=1




l = []
record_count = 0
while True:
    print("\nWelcome To Pattern Printing")
    action = input("'1' - Pattern 1\n'2' - Pattern 2\n'3' - Pattern 3"
                   "\n'4' - Pattern 4\n'5' - Pattern 5\n'6' - Pattern 6\n'7' - Quit\nEnter Your Choice==>")
    if action == '1':
        pattern_1()

    elif action == '2':
        pattern_2()

    elif action == '3':
        pattern_3()
    elif action == '4':
        pattern_4()
    elif action == '5':
        pattern_5()
    elif action == '6':
        pattern_6()
    elif action == '7':
        print("Thank You!!\n")
        break
    else:
        print("Incorrect choice??\n")