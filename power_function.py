def power_function(base, power):
    result = 1
    for i in range(power):
        result *= base
    return result


base = int(input("Give the base number: "))
power = int(input("Give the power number: "))
print(power_function(base, power))