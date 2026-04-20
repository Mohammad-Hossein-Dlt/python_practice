
def upsidedown(smaller_number: str, biger_number: str) -> int:
    rules = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    def smaller_equal(a: str, b: str) -> bool:
        if len(a) != len(b):
            return len(a) < len(b)
        return a <= b

    def build(n: int, m: int) -> list[str]:
        if n == 0:
            return [""]
        if n == 1:
            return ["0", "1", "8"]
        
        middles = build(n - 2, m)
        res = []
        for mid in middles:
            for a, b in rules.items():
                if n == m and a == "0":
                    continue
                res.append(a + mid + b)
        return res

    counter = 0
    for length in range(len(smaller_number), len(biger_number) + 1):
        for num in build(length, length):
            if smaller_equal(smaller_number, num) and smaller_equal(num, biger_number):
                counter += 1
    return counter

print(upsidedown('10','100')) 
