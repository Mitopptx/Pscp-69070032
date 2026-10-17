"""balling"""
def main():
    """:3"""
    lock = True
    count=0
    while True:
        word = input()
        if word == "END":
            break
        if word =="C" and lock:
            lock = False
        if word == "P" and not lock:
            lock = True
            count +=1
    print(count)
main()
