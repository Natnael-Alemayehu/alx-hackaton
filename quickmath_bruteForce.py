def quickMath(length,lst1):
    for i in range(length - 2):
        for j in range(i, length -1):
            for k in range(j, length):
                if lst1[i] + lst1[j] + lst1[k] == 0:
                    return "DA"
    return "NU"

num_lists = int(input().strip()) 

results = []  
for _ in range(num_lists):
    length = int(input().strip())  
    lst = list(map(int, input().strip().split()))  
    results.append(quickMath(length, lst)) 

# Print results for each list
for result in results:
    print(result)

# print(quickMath(6, [7,9,12,-6,-9,-6]))
        