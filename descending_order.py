
def descending_order(num: int) -> int:
    num = abs(num)
    if num == 0:
        return 1
    
    numbers = []
    
    while num > 0:
        numbers.append(num % 10)
        num //= 10
    
    numbers.sort(reverse=True)
    
    result = 0
    for i in numbers:
        result = result * 10 + i
    
    return result


print(descending_order(7482053916))