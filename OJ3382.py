"""Null"""
def main():
    """o-o"""
    arr =[]
    word =""
    while word != "NULL":
        word = input()
        arr.append(word)
    for i in range(len(arr)-2,-1,-1):
        print(arr[i])
main()
