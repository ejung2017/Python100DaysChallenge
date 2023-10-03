filename = "uni.uni.net - - [234] Get 200 6000"

list1 = list(filename.split(" "))
print(list1)
count = 0
total_bytes = 0
if int(list1[-1]) > 5000: 
    count += 1 
    total_bytes = int(list1[-1])

print(count, total_bytes)