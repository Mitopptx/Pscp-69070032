"""resistor"""
def main():
    """:3"""
    colors = {"Black": 0,"Brown": 1,"Red": 2,"Orange": 3,"Yellow": 4,
        "Green": 5,"Blue": 6,"Purple": 7,"Grey": 8,"White": 9}
    mul = {"Black": 1,"Brown": 10,"Red": 100,"Orange": 1000,"Yellow": 10000,
        "Green": 100000,"Blue": 1000000,"Gold": 0.1,"Silver": 0.01}
    tol= {"Brown": 0.01,"Red": 0.02,"Green": 0.005,"Blue": 0.0025,
        "Purple": 0.001,"Grey": 0.00005,"Gold": 0.05,"Silver": 0.1}
    arr=[""]*4
    for i in range(4):
        color = input()
        arr[i] = color
    if arr[0] not in colors or arr[1] not in colors or arr[2] not in mul or arr[3] not in tol:
        print("Error")
        return
    number = (colors[arr[0]]*10)+colors[arr[1]]
    number *= mul[arr[2]]
    tole = number * tol[arr[3]]
    print(f"{(number-tole):.4f}")
    print(f"{(number+tole):.4f}")
main()
