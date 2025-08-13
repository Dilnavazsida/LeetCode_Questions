def missing_num(num):
    n=len(num)

    acpected_sum = n * (n+1) // 2

    sm = sum(num)
    missing_num = acpected_sum-sm

    return missing_num
n = [3, 0, 1]
print("Missing num is :",missing_num(n))