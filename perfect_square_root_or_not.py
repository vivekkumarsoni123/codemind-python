import math
n=int(input())
r = math.trunc(math.sqrt(n))
if(r*r == n) :
    print("True")
else:
    print("False")