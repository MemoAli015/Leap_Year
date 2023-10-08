def is_leap(n:int) -> int:
    if n % 4 == 0:
        return True
    if n % 400 == 0:
        return True
    if n % 100 in range(0,100):
        return False
   
n = int(input())
print(is_leap(n))