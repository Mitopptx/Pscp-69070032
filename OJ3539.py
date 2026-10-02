"""IPHONE COLD DIH"""
def main():
    """:3"""
    phone = input()
    storage = input()
    if storage == "1 TB":
        storage = 1024
    else:
        storage,_ = storage.split()
        storage = int(storage)
    if phone == "iPhone 13 mini" and storage in (128,256,512):
        price = 25900
    elif phone == "iPhone 13" and storage in (128,256,512):
        price = 29900
    elif phone == "iPhone 13 Pro" and storage in (128,256,512,1024):
        price = 38900
    elif phone == "iPhone 13 Pro Max" and storage in (128,256,512,1024):
        price = 42900
    else:
        print("Not Available")
        return
    if storage == 128:
        print(price)
    elif storage == 256:
        print(price +4000)
    elif storage == 512:
        print(price + 12000)
    elif storage == 1024 and phone in ("iPhone 13 Pro","iPhone 13 Pro Max"):
        print(price + 20000)
    else:
        print("Not Available")
        return
main()
