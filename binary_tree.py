import time
from functools import lru_cache
#least recently used cache

# @lru_cache(maxsize=15000)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

# memo_fib = {}

# def fib_memo(n):
#     if n in memo_fib:
#         return memo_fib[n]
    
#     else:
#         if n==1 or n == 2:
#             memo_fib[n] = 1
#             return memo_fib[n]
#         else:
#             memo_fib[n] = fib_memo(n-1) + fib_memo(n-2)
#             return memo_fib[n]

start= time.time()

print(fib(40))

end = time.time()

print(end - start) 

# start= time.time()

# print(fib_memo(1000))

# end = time.time()

# print(end - start)