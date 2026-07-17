"""SAitama"""
import math
wit =int(input())
sit =int(input())
ruk =int(input())
run =int(input())
Swit =int(input())
Ssit =int(input())
Srun =int(input())
Sruk =int(input())
Cal={'a':math.ceil(wit/Swit) ,'b':math.ceil(sit/Ssit),
    'c':math.ceil(ruk/Sruk),'d':math.ceil(run/Srun)}
print(max(Cal.values()))
