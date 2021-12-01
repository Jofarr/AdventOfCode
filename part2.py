def advent1():
    f = open('AdventDay1.txt', 'r')
    x = f.read().split("\n")
    f.close()
    print(x)
    count = 0
    for i in range(3, len(x)):
        sum1 = int(x[i-1]) + int(x[i-2]) + int(x[i-3])
        sum2 = int(x[i]) + int(x[i-1]) + int(x[i-2])
        if sum1 < sum2:
            count +=1
    
    print(count)

print(advent1())