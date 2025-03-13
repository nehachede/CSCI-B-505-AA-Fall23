def kthSmallest(arr, k):
    
    import heapq
    
    if k not in range (0,len(arr)):
        return -1
    heapq.heapify(arr)

    return heapq.nsmallest(k, arr)[-1]