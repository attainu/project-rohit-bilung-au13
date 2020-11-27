import welcome
import book
import update
import check

again = "Y"
check.cab=0
while again.upper() == "Y":
    user = welcome.display()
    if user == 1:
        name=input("enter name : ")
        if check.cab==1:
            book.booking(name)
        else:
            print("no cabs available, wait for cab to be available")
    elif user == 2:
        name=input("enter name : ")
        check.checkAvail(name)
    else:
        print("enter correct format")
    again = input("Do you want to continue press y or press n to exit ")
print("\nThank you for choosing our service ")