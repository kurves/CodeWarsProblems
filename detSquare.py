import math
def detSquare(num):
    if num < 0:
        print("False")
    n = math.sqrt(num)
    if num % n == 0:
        print("true") 
    

detSquare(-1)
