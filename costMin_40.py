def costMin(n,m,lst1, lst2): 
    if n > m:
        lst1, lst2 = lst2, lst1
        n,m = m,n

    cost = m

    for num in lst2:
        if num in lst1:
            cost = cost - 1
    
    return cost

n, m = map(int, input().strip().split())   
lst1 = list(map(int, input().strip().split())) 
lst2 = list(map(int, input().strip().split())) 


print(costMin(n, m, lst1, lst2))