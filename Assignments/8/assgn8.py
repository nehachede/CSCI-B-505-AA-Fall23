def translate_message(arr):
    inp = set(arr)
    value = 0
    
    for i in arr:
        if i - 7 not in inp:
            j, new_v = i, 1
            
            while j + 7 in inp:
                j += 7
                new_v += 1
            value = max(value, new_v)
    return value

def find_order_size(orders):
    v, sym = set(), set()

    for i in orders:
        if tuple(i)[::-1] in v or tuple(i) in sym:
            sym.add(tuple(i))
        v.add(tuple(i))

    return len(orders) - len(sym)

from collections import Counter

def findCircusStrings(s):
    subs = set()
    subs_c = Counter()

    for i in range(len(s) - 9):
        subs.add(s[i:i + 10])
        subs_c[s[i:i + 10]] += 1

    return sorted([i for i in subs if subs_c[i] > 1])

def aliveOrDead(trees, tigersWish):
    inp = [int(x) if x != 'X' else None for x in trees]
    d = {}

    for i, j in [(i, j) for i in range(len(inp)) for j in range(i + 1, len(inp))]:
        if None in (inp[i], inp[j]):
            continue

        if (tigersWish - (inp[i] + inp[j])) in d:
            if not any(i in k or j in k for k in d[tigersWish - (inp[i] + inp[j])]):
                return 'Alive'

        d.setdefault((inp[i] + inp[j]), []).append((i, j))

    return 'Dead'