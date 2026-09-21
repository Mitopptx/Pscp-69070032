"""Help kitchen"""
def main():
    """:3"""
    menu=[]
    while True:
        order = input()
        if order =="DONE":
            break
        if order =="CLOSED":
            menu.clear()
            break
        if order =="SOMETHING'S WRONG":
            menu.clear()
        elif order[:9] == "Can't do:":
            name = order[10:]
            if name in menu:
                menu.remove(name)
        else:
            name ,index = order.split(" #")
            if index == "N":
                menu.append(name)
            else:
                index = int(index)-1
                menu.insert(index,name)
    if not menu:
        print("Full Course: [] Reversed: []")
    else:
        print("Full Course: ['",end="")
        print(*menu,sep="', '",end="")
        print("'] Reversed: ['",end="")
        print(*menu[::-1],sep="', '",end="']")
main()
