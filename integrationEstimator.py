inc = 1

displacement = 2

total = 0

for i in range(int(displacement/inc)):
    x = (i+1)*inc + 0
    # print('x: ', x)
    area = inc * (1-(x-1)**(2))**(1/2)
    # print('area :', area)
    total += area

print("total: ", total)