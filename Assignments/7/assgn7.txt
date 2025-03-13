from typing import List
import heapq

def specialHub(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    d = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            d[i][j] = float('inf')

    for i in range(len(edges)):
        c1, c2, w = edges[i]
        d[c1][c2] = d[c2][c1] = w
        d[c1][c1] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] == float('inf') or d[k][j] == float('inf'):
                    continue
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    minc, cityNumber = n, -1

    for i in range(n):
        if sum(1 for c in range(n) if d[i][c] <= distanceThreshold) < minc or (sum(1 for c in range(n) if d[i][c] <= distanceThreshold) == minc and i > cityNumber):
            minc, cityNumber = sum(1 for c in range(n) if d[i][c] <= distanceThreshold), i

    return cityNumber

def challenge(n: int, connections: List[List[int]]) -> int:
    g = {}
    for c in connections:
        x, y, w = c[0] - 1, c[1] - 1, c[2]
        g.setdefault(x, []).append((y, w))
        g.setdefault(y, []).append((x, w))
    print(g)

    v = [False] * n
    pq = [(0, 0)]
    minimumCost, totv = 0, 0

    while pq:
        i, w = heapq.heappop(pq)
        if not v[i]:
            minimumCost += w
            v[i] = True
            totv += 1
            
            if i in g:
                for k, we in g[i]:
                    print(k,we)
                    if not v[k]:
                        heapq.heappush(pq, (k, we))

    return minimumCost if totv == n else -1

def min_cost_to_supply_water(n, wells, pipes):
    tot = [i for i in pipes] + [[0, i + 1, wells[i]] for i in range(n)]
    tot.sort(key=lambda x: x[2])

    p = [i for i in range(n + 1)]

    min_cost = 0
    for x in tot:
        if p[x[0]] == p[x[1]]:
            continue
        min_cost += x[2]
        for k in range(n + 1):
            if p[k] == p[x[0]]:
                p[k] = p[x[1]]
        n -= 1
        if n == 0:
            break

    return min_cost

def cheapestRoutes(s, prices):
    min_prices = [-1] * len(prices)
    min_prices[s] = 0

    pq = [(0, s)]

    while pq:
        p, c = heapq.heappop(pq)

        if min_prices[c] != -1 and p > min_prices[c]:
            continue

        for adj_c in range(len(prices)):
            adj_p = prices[c][adj_c]

            if adj_p == -1:
                continue

            new_p = p + adj_p

            if min_prices[adj_c] == -1 or new_p < min_prices[adj_c]:
                min_prices[adj_c] = new_p
                heapq.heappush(pq, (new_p, adj_c))

    return min_prices

def isDividePossible(n, connected_houses):
    def dfs(house, fl):
        if house in v:
            return v[house] == fl

        v[house] = fl
        return all(dfs(i, 1 - fl) for i in g[house])

    g, v = {}, {}
    for h in connected_houses:
        if h[0] not in g:
            g[h[0]] = []
        if h[1] not in g:
            g[h[1]] = []
        g[h[0]].append(h[1])
        g[h[1]].append(h[0])


    return all(i in v or dfs(i, 0) for i in range(n))

def minCostToConnectHubs(hubs):
    def lookup(n):
        while e[n] != n:
            n = e[n]
        return n
    
    dist, i = 0, 0
    mat, w = list(hubs), []
    
    for i in range(len(mat)):
        for j in range(i + 1, len(mat)):
            w.append((i, j, abs(mat[i][0] - mat[j][0]) + abs(mat[i][1] - mat[j][1])))

    w.sort(key = lambda x: x[-1])
    
    e = [i for i in range(len(mat))]
    
    for k in w:
        if lookup(k[0]) != lookup(k[1]):
            e[lookup(k[1])] = lookup(k[0])
            dist += k[2]
    
    return dist

def findMaxSuccessPath(n, edges, prob, start_node, end_node):
    g = {i: [] for i in range(n)}

    for i in edges:
        a, b = i
        g[a].append((b, prob[edges.index(i)]))
        g[b].append((a, prob[edges.index(i)]))

    q = [(-1, start_node)]
    v = [False] * n

    while q:
        p, sat = heapq.heappop(q)
        p = -p

        if sat == end_node:
            return p

        if v[sat]:
            continue

        v[sat] = True

        for i, p_i in g[sat]:
            heapq.heappush(q, (-p * p_i, i))

    return 0.0

def minimumTimeToVisit(grid):
    m, n = len(grid), len(grid[0])
    
    if grid[1][0] > 1 and grid[0][1] > 1:
        return -1
    
    hp = [(0, 0, 0)]

    while hp:
        tm, r_n, c_n = heapq.heappop(hp)
        tm += 1

        for i, j in ((r_n - 1, c_n), (r_n + 1, c_n), (r_n, c_n - 1), (r_n, c_n + 1)):
            if 0 <= i < m and 0 <= j < n and grid[i][j] != -1:
                nxt = max(tm, grid[i][j] + (1 if (tm + grid[i][j]) % 2 else 0))
                
                if i == m - 1 and j == n - 1:
                    return nxt
                
                heapq.heappush(hp, (nxt, i, j))
                grid[i][j] = -1

    return -1

def WeightLimitedPathsExist(n, edgelist, querylist):
    g = {i: [] for i in range(n)}

    def dfs(p, q, w, v):
        v.append(p)

        if p == q:
            return True

        for i, wi in g[p]:
            if i not in v and wi >= w:
                if dfs(i, q, w, v):
                    return True

        return False
    
    for e in edgelist:
        g[e[0]].append((e[1], e[2]))
        g[e[1]].append((e[0], e[2]))

    return [dfs(p, q, w, []) for p, q, w in querylist]

def shortestFareRoute(start, target, specialRoads):
    
    min_fare = abs(target[0] - start[0]) + abs(target[1] - start[1])
    
    br = []
    for x1, y1, x2, y2, c in specialRoads:
        br.append([(abs(target[0] - x2) + abs(target[1] - y2) + c), c, x1, y1, x2, y2])
        
    hp = [(0, start[0], start[1])]
    v = {(start[0], start[1]): 0}
    
    while hp:
        temp_d, x, y = heapq.heappop(hp)
        if temp_d >= min_fare:
            continue            
        
        for diff, c, x1, y1, x2, y2 in br:
            if (x2, y2) not in v or (abs(x1 - x) + abs(y1 - y) + temp_d + c) < v[(x2, y2)]:
                heapq.heappush(hp, ((abs(x1 - x) + abs(y1 - y) + temp_d + c), x2, y2))
                v[(x2, y2)] = (abs(x1 - x) + abs(y1 - y) + temp_d +  c)
            min_fare = min(min_fare, (abs(x1 - x) + abs(y1 - y) + temp_d + diff))
    
    return min_fare