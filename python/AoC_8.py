len_total = 0
len_eval = 0

for line in open('AoC_8.in', 'r'):
    len_total += len(line.strip())
    len_eval += len(eval(line.strip()))

print(len_total - len_eval)
