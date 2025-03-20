#PS: Contact App Dictionary using Dictionary Data Structure

import json

def modify1():
    global l
    if len(l)==0:
        print("Contact List is Empty!!\n")
    else:
        num = input("Enter Adhar Number to be Modify: ")
        found = 0
        for i in range(0,len(l)):
            if num == l[i]['adhar']:# Matching entered Addhar Number with Dictionary with Addhar No. which is present
                        # at i th position of List
                found+=1
                d1 = {
                    'name': input("Enter New Name==>"),
                    'adhar': input("Adhar New Number==>"),
                    'mb': input("Mobile New Number==>"),
                    'addr': input("New Address==>"),
                    'date': input("New Date of Birth(DD/MM/YYY): ")
                    }
                l[i] = d1
                if num == l[i]['adhar']:
                    print("Record Modified Successfully With Adhar Number: ", num,"\n")
                else:
                    print("Record Modified Successfully With NEW Adhar Number: ",l[i]['adhar'],"\n")
                break
        if found == 0:
            print("Record With Adhar Number: ",num," is Not Present")


def search():
    global l
    if len(l)==0:
        print("Contact List is Empty!!\n")
    else:
        num = input("Enter Adhar Number to be Search==>")
        found = 0
        for i in range(0,len(l)):
            if num == l[i]['adhar']:# Matching entered Addhar Number with Dictionary with Addhar No. which is present
                        # at i th position of List
                found+=1
                print("Record Has been Found with Addhar Number: ", l[i]['adhar'],"\n")
                print("Details are as Follows")
                print("**********************************")
                print("Record No : ", i + 1)
                print("Name :", l[i]['name'])
                print("Adhar Number :", l[i]['adhar'])
                print("Mobile Number :", l[i]['mb'])
                print("Address :", l[i]['addr'])
                print("Date of Birth:", l[i]['date'])
                print("**********************************\n")
                break
        if found == 0:
            print("Record With Adhar Number: ",num," is Not Present\n")



def del1():
    found = 0
    num = None
    global l
    if len(l)==0:
        print("Contact List is Empty!!\n")
    else:
        num = input("Enter Adhar Number to be Deleted: ")

        for i in range(0,len(l)):
            if num == l[i]['adhar']:# Matching entered Addhar Number with Dictionary with Addhar No. which is present
                        # at i th position of List
                found+=1
                print("\nRecord Has been Deleted with Addhar Number: ", l[i]['adhar'],"\n")
                del l[i]
                break
    if found == 0:
        print("\nRecord With Adhar Number: ",num," is Not Present\n")


def view():# To Display All the Records
    global l
    if len(l)==0:
        print("\nContact List is Empty!!\n")
    else:
        print("************************************\n")
        print("List having Total Record Count: ",record_count)
        print("\n************************************")
        while True:
            choice = input("'1' - View Regular Format\n'2' - View Json Format\n'3' - Quit\nEnter Your Choice==>")
            if choice == '1':
                    print("All Contacts\n")
                    for i in range(0, len(l)):
                        print("**********************************")
                        print("Record No : ", i + 1)
                        print("Name :", l[i]['name'])
                        print("Adhar Number :", l[i]['adhar'])
                        print("Mobile Number :", l[i]['mb'])
                        print("Address :", l[i]['addr'])
                        print("Date :", l[i]['date'])
                        print("**********************************\n")

            elif choice == '2'or choice == 'v' or choice == 'V':
                    print("\n\nThis is Json Format")
                    print(json.dumps(l,indent=4))

            elif choice == '3'or choice == 'q' or choice == 'Q':
                print("Thank You!!\n")
                break
            else:
                print("Incorrect choice!!\n")


def add():
    global record_count,l
    d1={ #Dictionary Data Type to Create Structure of Record, Creating Dictionary d1
        'name' : input("Enter Full Name: "),
        'adhar': input("Enter Adhar Number: "),
        'mb' : input("Enter Mobile Number: "),
        'addr' : input("Enter Address: "),
        'date' : input("Enter Date of Birth(DD/MM/YYYY): ")
        }
    print("\n")
    l+=[d1] # Creating a List of Dictionary where List is l and Dictionary d1
    record_count +=1 # to maintain total record count in list


# Record Creating App.
l = []
record_count = 0
while True:
    print("\nWelcome To Record Keeping App")
    action = input("'a' - Add Contact\n'd' - Delete Contact\n'v' - View All Contact"
                   "\n's' - Search Contact\n'm' - Modify Contact\n'q' - Quit\nEnter Your Choice==>")
    if action == 'a' or action == 'A':
        add()

    elif action == 'd' or action == 'D':
        del1()

    elif action == 'v' or action == 'V':
        view()
    elif action == 's' or action == 'S':
        search()
    elif action == 'm' or action == 'M':
        modify1()
    elif action == 'q' or action == 'Q':
        print("Thank You!!\n")
        break
    else:
        print("Incorrect choice??\n")
