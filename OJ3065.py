num = int(input())
if num<0:
  print("Error : Please input positive number")
elif not num or num>9:
  print("Error : Out of range")
else:
    ber=''
    for i in range(num):
        ber += 'I'
        if ber == 'IIII':
          ber = 'IV'
        elif ber == 'IVI':
          ber = 'V'
        elif ber == 'VIIII':
          ber = 'IX'
    print(ber)
