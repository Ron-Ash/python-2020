fibnum = [1, 1]

fibnuminv = [1, 1]

fibTotal = 0

for i in range(1000):
    fibnum.append(fibnum[i]+fibnum[i+1])
    fibnuminv.append(fibnum[i+2]**(-1))
    fibTotal += fibnuminv[i]

print(fibTotal)
