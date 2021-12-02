def advent1():
    f = open('AdventDay1.txt', 'r')
    x = f.read().split("\n")
    f.close()
    print(x)
    count = 0
    for i in range(1, len(x)):
        if (int(x[i]) > int(x[i-1])):
            count +=1
    
    print(count)

print(advent1())
