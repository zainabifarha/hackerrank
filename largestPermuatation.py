n, k = map(int, input().split())
inputArray = list(map(int, input().split()))
indexArray = [0] * (n + 1)

if k < n:
    for i in range(n):
        indexArray[inputArray[i]] = i;
    i = 0
    count = 0
    while(count<k and i<n):
        if inputArray[i] != n - i:
            inputArray[indexArray[n - i]] = inputArray[i]
            indexArray[inputArray[i]] = indexArray[n - i]
            inputArray[i] = n - i
            count += 1
        i += 1
    for i in range(n):
        print(inputArray[i], end=" ")
else:
    for i in range(n):
        print (n - i, end=" ")
