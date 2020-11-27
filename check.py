import update

def checkAvail(name):
    global cab
    global dname
    dname=name
    cab=1
    if cab<1:
        print("no cabs for booking")
    else:
        print("cabs available for drive")
        update.upd()
