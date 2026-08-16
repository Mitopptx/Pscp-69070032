"""SUKI BONUS"""
status,year,salary=input().split()
year = int(year)
salary = int(salary)
if year <=5:
    per =4
elif year >=10:
    per=6
else:
    per=5
if status =="M":
    per += per//1.5
    print(1500+int(per*salary/100))
elif status == "B":
    per +=1
    print(1000+int(per*salary/100))
elif status == "G":
    print(500+int(per*salary/100))
