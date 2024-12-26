r1, r2, i1, r3, i2, i3, i4 = map(int, input("Enter numbers r1, r2, i1, r3, i2, i3, i4 through space: ").split())
s1 = (r1 + i1 + i2 + i4) % 2
s2 = (r2 + i1 + i3 + i4) % 2
s3 = (r3 + i2 + i3 + i4) % 2
syndrome_s = str(s1) + str(s2) + str(s3)

cases = ['000', '001', '010', '011', '100', '101', '110', '111']
cases_bits = ['not found', 'r3', 'r2', 'i3', 'r1', 'i2', 'i1', 'i4']
for i in range(len(cases)):
    if syndrome_s == cases[i]:
        problem_bit = cases_bits[i]
        break

if problem_bit == 'i1':
    i1 = (i1 + 1) % 2
elif problem_bit == 'i2':
    i2 = (i2 + 1) % 2
elif problem_bit == 'i3':
    i3 = (i3 + 1) % 2
elif problem_bit == 'i4':
    i4 = (i4 + 1) % 2

print('Correct message:', i1, i2, i3, i4)
print('Misspelled bit:', problem_bit)