def buyIceCream(costs, total):
    max_ice_creams = 0
    
    costs_s = costs
    tot = total
    
    for i in range(1, len(costs_s)):
        k = costs_s[i]
        j = i - 1
        
        print(i, k, j, costs_s[j])
        
        while j >=0 and k < costs_s[j]:
            costs_s[j+1] = costs_s[j]
            j -= 1
        
        costs_s[j+1] = k
    
    print(costs)
    print(costs_s)
    
    for c in costs_s:
        if tot >= c:
            tot -= c
            max_ice_creams += 1
        else:
            break
    
    return max_ice_creams
