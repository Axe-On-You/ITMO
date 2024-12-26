# Перевод из 10-значной в нега-10-значную
def decimal_to_neg_base10(n):
    result = ''
    while n != 0:
        remainder = n % -10
        if remainder < 0:
            remainder += 10
            n = (n - remainder) // -10
        else:
            n = n // -10
        result = str(remainder) + result
    return result

# Пример [перевод 61 (10) -> 141 (-10)]:
input_number = int(input("Enter your decimal number: "))
output_number = decimal_to_neg_base10(input_number)
print(f"The decimal number {input_number} in base -10 is {output_number}")

# Перевод из десятичной в симметричную 
def decimal_to_symmetric(n, base):
    digits = []
    while n:
        n, remainder = divmod(n, base)
        if remainder > base // 2:
            remainder -= base
            n += 1
        if remainder < 0:
            digits.append('{^' + str(-remainder) + '}')
        else:
            digits.append(str(remainder))
    return ''.join(reversed(digits))

# Пример [перевод 572 (10) -> 10{^2}{^1} (5C)]:
decimal_num = int(input("Enter your decimal number: "))
base = int(input("Enter base of symmetric system: "))
result = decimal_to_symmetric(decimal_num, base)
print(f"{decimal_num} in symmetric {base}-ary system is {result}")