def linear_search(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return "Found in position: "+ str(i)
    return -1

ans = linear_search([1,2,3,4,5], 9)

print(ans)