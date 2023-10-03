def getMaximumProfit(price, profit):
    # Write your code here
    n = len(price)
    long_int = 0
    if n < 3: 
        long_int = -1
    else: 
        for i in range(2,len(price)): 
            if price[i] > price[i-1] > price[i-2]: 
                long_int += profit[i] + profit[i-1] + profit[i-2]
    return long_int

getMaximumProfit(5,[3,4,5])