# Lst2 is the smaller list and lst1 is the bigger list

def costMin(n, m, lst1, lst2):
    if n > m:
        lst1, lst2 = lst2, lst1
        n, m = m, n

    max_value = 10**6
    howMany = [0] * (max_value + 1)

    for num in lst2:
        howMany[num] += 1

    cost = m

    for num in lst1:
        if howMany[num] > 0:

            cost -= 1

            howMany[num] -= 1

    return cost

n, m = map(int, input().strip().split())   
lst1 = list(map(int, input().strip().split())) 
lst2 = list(map(int, input().strip().split())) 


print(costMin(n, m, lst1, lst2))