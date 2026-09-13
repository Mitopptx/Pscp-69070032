"""money interchange with mrt"""
money = int(input())
ten = money//10
money -= (money//10)*10
five = money//5
money -= (money//5)*5
two = money//2
money -= (money//2)*2
print("10 = ",ten,"\n5 = ",five,"\n2 = ",two,"\n1 = ",money,sep='')
