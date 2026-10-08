"""figit"""
def main():
    """:3"""
    word = list(input.split())
    num1 = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    num2 = {"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19}
    total = ""
    for i in word:
        if i in num1:
            total += num1[i]
        elif i  in num2:
            total += num2[i]
        
main()
