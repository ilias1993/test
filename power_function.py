def power_function(base, power):
    result = 1
    for i in range(power):
        result *= base
    return result


base = input("Give the base number: ")
power = input("Give the power number: ")
print(power_function(int(base), int(power)))