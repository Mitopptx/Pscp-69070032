"""STOCKER"""
def main():
    """:3"""
    item = {}
    while True:
        word = input()
        if word == "END":
            break
        if word[:3] == "ADD":
            _,name,num = word.split()
            if name in item:
                item[name] += int(num)
                continue
            item[name] = int(num)
        if word[:6] == "REMOVE":
            _,name,num = word.split()
            if name not in item or int(num)>item[name]:
                print("Not enough stock for",name)
                item[name] = 0
                continue
            item[name] -= int(num)
        if word == "CHECK":
            item = dict(sorted(item.items()))
            check = True
            for i in item:
                if item[i]<5:
                    print(i)
                    check =False
            if check:
                print("All stocks are sufficient")
        if word == "REPORT":
            item = dict(sorted(item.items()))
            for i in item:
                print(i,": ",item[i],sep="")
main()
