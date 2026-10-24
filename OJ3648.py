"""kang"""
def main():
    """:3"""
    t = input().strip("[]")
    tin = list(t.split(", "))
    t = input().strip("[]")
    tout = list(t.split(", "))
    train = []
    size =0
    for i in range (len(tin)):
        if train:
            for j in train:
                if tin[i]>j:
                    train.remove(j)
        train.append(tout[i])
        if size<len(train):
            size = len(train)
    print(size)
main()
