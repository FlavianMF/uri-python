import math

n = int(input())

sqrt5 = math.sqrt(5)

fibo = (math.pow((1+sqrt5)/2, n) - math.pow((1-sqrt5)/2, n))/(sqrt5)

print("%.1f" % fibo)
