
# def factorial(
#     n: int,
# ) -> int:
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

def factorial(
    n: int,
) -> int:
    result: int = 1
    
    for i in range(1, n+1):
        result *= i
        
    return result
    
def sum_to_n(
    n: int,
) -> int:
    return (n * (n+1)) // 2

def choose(
    n: int,
    k: int,
) -> int:
    return factorial(n) // (factorial(k) * factorial(n - k))

print(choose(100_000_000, 3))