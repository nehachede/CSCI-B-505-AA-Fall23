import numpy

def minCostConnectPoints(points):
    dist = 0
    mat = numpy.asarray(points)
    
    w = []
    i = 0
    
    for i in range(len(mat)):
        for j in range(i + 1, len(mat)):
            # print(mat[i], mat[j])
            w.append((i, j, abs(mat[i][0] - mat[j][0]) + abs(mat[i][1] - mat[j][1])))

    w.sort(key = lambda x: x[-1])
    # print(w)
    
    e = [i for i in range(len(mat))]
    # print(e)
    
    def search(n):
        while e[n] != n:
            n = e[n]
        return n
    
    for k in w:
        if search(k[0]) != search(k[1]):
            e[search(k[1])] = search(k[0])
            dist += k[2]
    
    return dist

# print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
