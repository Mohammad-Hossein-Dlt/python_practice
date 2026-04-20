
def find_smallest(
    m: int,
) -> int:
    for n in range(1, m+1):
        if pow(n, n, m) == 0:
            return n
        
print(find_smallest(1234567890))