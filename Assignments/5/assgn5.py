import heapq
from collections import Counter

def busRemaining(busStation):
    if not busStation or len(busStation)<0 or len(busStation)>10000 or (all(i[0]<0 or i[1]>100000 for i in busStation)):
        return 0
    
    # print(busStation)
    # busStation.sort(key=lambda x: x[0])
    # print(busStation)
    
    remainingBuses = []
    curr = busStation[0]
    
    for i in range(1, len(busStation)):
        nxt = busStation[i]
        
        if curr[1] >= nxt[0]:
            curr = [curr[0], max(curr[1], nxt[1])]
        else:
            remainingBuses.append(curr)
            curr = nxt
    
    remainingBuses.append(curr)
    print(remainingBuses)
    return len(remainingBuses)

def solvePuzzle(numbers):
    if len(numbers) < 1 or len(numbers) > 10000:
        return 0
    if any(num < 1 or num > 100000 for num in numbers):
        return 0
    
    answerToPuzzle = 0
    
    ind = [0] * len(numbers)

    min_heap = [(numbers[i], i) for i in range(len(numbers))]
    heapq.heapify(min_heap)

    while sum(ind) != len(numbers):
        while min_heap:
            num, idx = heapq.heappop(min_heap)
            if not ind[idx]:
                break

        ind[idx] = 1
        answerToPuzzle += num
        for j in range(max(0, idx - 1), min(len(numbers), idx + 2)):
            ind[j] = 1

    return answerToPuzzle

def findMedianPrice(prices, k):
    medians, lh, rh = [], [], []

    for i in range(len(prices)):
        if not rh or prices[i] <= -rh[0]:
            heapq.heappush(rh, -prices[i])
        else:
            heapq.heappush(lh, prices[i])
        
        if len(rh) > len(lh) + 1:
            heapq.heappush(lh, -heapq.heappop(rh))
        elif len(lh) > len(rh):
            heapq.heappush(rh, -heapq.heappop(lh))
        
        if i >= k - 1:
            if len(rh) > len(lh):
                med = -rh[0]
            elif len(lh) > len(rh):
                med = lh[0]
            else:
                med = (-rh[0] + lh[0]) / 2.0
            
            medians.append(med)
            
            if prices[i - k + 1] <= -rh[0]:
                rh.remove(-prices[i - k + 1])
            else:
                lh.remove(prices[i - k + 1])
                
            if len(rh) > len(lh) + 1:
                heapq.heappush(lh, -heapq.heappop(rh))
            elif len(lh) > len(rh):
                heapq.heappush(rh, -heapq.heappop(lh))
    
    return medians

def shorterBuildings(heights):
    def msort(inp):
        if len(inp) <= 1:
            return inp

        mid = len(inp) // 2
        l = inp[:mid]
        r = inp[mid:]

        return merge(msort(l), msort(r))

    def merge(l, r):
        result = []
        i = j = 0
        while i < len(l) or j < len(r):
            if j == len(r) or (i < len(l) and l[i][1] <= r[j][1]):
                result.append(l[i])
                res[l[i][0]] += j
                i += 1
            else:
                result.append(r[j])
                j += 1
        return result

    n = len(heights)
    res = [0] * n
    inp = list(enumerate(heights))
    msort(inp)
    
    return res

def determineStandardRadius(houses, heaters):
    def qsort(inp):
        if len(inp) <= 1:
            return inp
        else:
            pv = inp[0]
            l = [i for i in inp[1:] if i < pv]
            r = [i for i in inp[1:] if i >= pv]
            return qsort(l) + [pv] + qsort(r)

    def b_sch(a, k):
        l, r = 0, len(a) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if a[mid] < k:
                l = mid + 1
            else:
                r = mid - 1
        return l

    res = 0
    s_ho = qsort(houses)
    s_he = qsort(heaters)
    
    for i in s_ho:
        h_idx = b_sch(s_he, i)
        if h_idx == 0:
            res = max(res, s_he[0] - i)
        elif h_idx == len(s_he):
            res = max(res, i - s_he[-1])
        else:
            l = i - s_he[h_idx - 1]
            r = s_he[h_idx] - i
            res = max(res, min(l, r))

    return res

def isRearrangePossible(s, k):
    def push_into_hp(inp, val):
        node = len(inp)
        inp.append(val)

        while node > 0:
            pnode = (node - 1) // 2
            if inp[pnode] <= inp[node]: 
                break
            inp[node], inp[pnode] = inp[pnode], inp[node]
            node = pnode
            pass
        pass

    def pop_from_hp(inp):
        ret = inp[0]
        lnode = inp.pop()
        
        if len(inp) == 0: 
            return ret

        inp[0] = lnode
        node = 0

        while True:
            ch1 = 2 * node + 1
            if ch1 >= len(inp): 
                return ret
            
            ch2 = ch1 + 1
            cnode = ch2 if ch2 < len(inp) and inp[ch2] < inp[ch1] else ch1
            
            if inp[node] <= inp[cnode]: 
                return ret
            inp[cnode], inp[node] = inp[node], inp[cnode]
            node = cnode
            pass
        pass

    temp_heap_max = []
    freq = Counter(s)

    for eng_alph, eng_alph_freq in freq.items():
        push_into_hp(temp_heap_max, (-eng_alph_freq, eng_alph))

    res = []

    while temp_heap_max:
        temp = []

        for _ in range(min(k, len(s) - len(res))):
            if not temp_heap_max:
                return len(res) == len(s)
            eng_alph_freq, eng_alph = pop_from_hp(temp_heap_max)
            res.append(eng_alph)
            if eng_alph_freq + 1 < 0:
                temp.append((eng_alph_freq + 1, eng_alph))

        for i in temp:
            push_into_hp(temp_heap_max, i)
    
    return len(res) == len(s)

class Huffman():
    def __init__(self):
        self.huffman_codes = {}
        self.source_string = ""

    def set_source_string(self, src_str):
        self.source_string = src_str

    def generate_codes(self):
        freq = Counter(self.source_string)
        hp = [[freq[c], [c,""]] for c in freq]

        heapq.heapify(hp)

        while len(hp) > 1:
            l = heapq.heappop(hp)
            r = heapq.heappop(hp)
            for i in l[1:]:
                i[1] = '0' + i[1]
            for i in r[1:]:
                i[1] = '1' + i[1]
            heapq.heappush(hp, [l[0] + r[0]] + l[1:] + r[1:])

        self.huffman_codes = dict(hp[0][1:])

    def encode_message(self, inp):
        return "".join(self.huffman_codes.get(c, '') for c in inp)

    def decode_message(self, inp):
        dmsg = ""
        c_inp = ""
        i = 0
    
        while i < len(inp):
            c_inp += inp[i]
            i += 1
    
            if c_inp in self.huffman_codes.values():
                dmsg += next(c for c, fr in self.huffman_codes.items() if fr == c_inp)
                c_inp = ""
    
        return dmsg

