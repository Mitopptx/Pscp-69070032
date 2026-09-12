"""bowl"""
def main():
    """bowkylion"""
    n = int(input())
    number = []
    count = []
    for _ in range(n):
        num = int(input())
        number.append(num)
    for i in number:
        counter = 0
        for j in range(n):
            if number[j] == i:
                counter+=1
        count.append(counter)
    print(max(count))
main()
