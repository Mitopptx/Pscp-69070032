"""figit"""
def main():
    """:3"""
    word = input()
    number = word.split()
    num1 = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    num2 = {"ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,
        "seventeen":17,"eighteen":18,"nineteen":19,"twenty":20,"thirty":30,"forty":40,
        "fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90}
    total = 0
    for i in number:
        if i in num1:
            total += num1[i]
        elif i  in num2:
            total += num2[i]
        elif i == "hundred" and "thousand" not in number:
            total *= 100
        elif i == "hundred":
            temp= total%1000
            total -= temp
            total += temp*100
        elif i == "thousand":
            total *= 1000
    print(total)
main()
