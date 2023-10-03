def subsetA(arr):
    arr.sort(reverse=True)
    sum1 = 0
    sum2 = 0
    # print(arr)
    for i in range(len(arr)): 
        sum1 += arr[i]
    # print(sum1)
    for i in range(len(arr)): 
        sum1 -= arr[i]
        sum2 += arr[i]
        print(arr[i])
        if sum2 > sum1:
            break
    # print(sum1)
    # print(sum2)

subsetA([5, 4, 7, 2, 3])

