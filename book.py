
import math
import location

def booking(name):
    print("hii",name,"Book Cab within 6kms")
    print("for cab booking set your location by x,y value eg: 2,5 ir 3,7")
    l=input()
    k=location.locations()
    print(k)
    print(l)
    p1=k.split(",")
    p2=l.split(",")
    distance = math.sqrt(((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1]))**2))
    rs=round(distance,2)
    if rs>6:
        print("your distance is",rs,"kms \nsorry!! cannot book beyond 6kms")
    else:
        print("your distance is",rs,"kms")
        print("your total price is",rs*10,"rupees" )
