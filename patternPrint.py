

def pattern_1():
    i = 1
    str_1 = []
    str_2 = ""
    j = 1
    while i!=6:
        j=i
        p = 0
        p = len(range(0, j))
        while(p!=0):
            str_1 +=[i]
            p-=1
        str_2 = ' '.join(map(str, str_1))
        print(str_2)
        del str_1[:]
        i +=1


def pattern_2():
    i = 1
    str_1 = []
    str_2 = ""
    j = 1
    k = 0
    while i!=6:
        j=i
        p = 0
        p = len(range(0, j))
        while(p!=0):
            str_1 +=[k+1]
            k += 1
            p-=1
        str_2 = ' '.join(map(str, str_1))
        print(str_2)
        del str_1[:]
        k = 0
        i +=1


def pattern_5():
    i = 5
    str_1 = []
    str_2 = ""
    j = 1
    while i!=0:
        j=i
        p = 0
        p = len(range(0, j))
        while(p!=0):
            str_1 +=[i]
            p-=1
        str_2 = ' '.join(map(str, str_1))
        print(str_2)
        del str_1[:]
        i -=1

def pattern_4():
    i = 5
    str_1 = []
    str_2 = ""
    j = 1
    k = 5
    while i!=0:
        j=i
        p = 0
        p = len(range(0, j))
        while(p!=0):
            str_1 +=[k]
            p-=1
        str_2 = ' '.join(map(str, str_1))
        print(str_2)
        del str_1[:]
        i -=1



def pattern_3():
    i = 5
    str_1 = []
    str_2 = ""
    j = 1
    k = 1
    while i!=0:
        j=i
        p = 0
        p = len(range(0, j))
        while(p!=0):
            str_1 +=[k]
            p-=1
        str_2 = ' '.join(map(str, str_1))
        print(str_2)
        del str_1[:]
        i -=1
        k +=1

def pattern_6():
    i = 6
    str_1 = []
    str_2 = ""
    j = 1
    k = 0
    while i!=0:
        j=i
        p = 0
        p = len(range(0, j))
        while(p!=0):
            str_1 +=[k]
            k +=1
            p-=1
        str_2 = ' '.join(map(str, str_1))
        print(str_2)
        del str_1[:]
        i -=1
        k = 0




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