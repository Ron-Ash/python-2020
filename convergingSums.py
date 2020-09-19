

# X_(n+1) = X_(n)/a ---> b/(a**0), b/(a**1), b/(a**2), ...
# X_(0) = b
# If -1>a>1 : b/(a**0) + b/(a**1) + b/(a**2) + ... = (a*b)/(a-1)

total = 0
values = [13, ]
decreasingFactor = -3.7869

for i in range(100000):
    values.append(values[i]/decreasingFactor)
print("The infinite sum: ", sum(values))
print("The prediction: ", decreasingFactor*values[0]/(decreasingFactor-1))


    
