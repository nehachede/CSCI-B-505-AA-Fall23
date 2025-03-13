def province(isConnected):
    def dfs(c):
        v[c] = True
        for i in range(len(isConnected)):
            if isConnected[c][i] == 1 and not v[i]:
                dfs(i)

    v = [False] * len(isConnected)
    p = 0
    
    for c in range(len(isConnected)):
        if not v[c]:
            dfs(c)
            p += 1
    
    return p
print(province([[1,1,0],[1,1,0],[0,0,1]]))
print(province([[1,0,0],[0,1,0],[0,0,1]]))
