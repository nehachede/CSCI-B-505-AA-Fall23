# 1
def MaximumDeafPeople(PeopleShout):
    maximumDeafCount = 0

    for i in range(len(PeopleShout)):
        visit = [False] * len(PeopleShout)
        visit[i] = True
        stack = [i]
        temp = 1

        while stack:
            k = stack.pop()

            for j in range(len(PeopleShout)):
                if not visit[j] and ((PeopleShout[k][0] - PeopleShout[j][0]) ** 2 + (PeopleShout[k][1] - PeopleShout[j][1]) ** 2) <= PeopleShout[k][2] ** 2:
                    visit[j] = True
                    stack.append(j)
                    temp += 1

        maximumDeafCount = max(maximumDeafCount, temp)

    return maximumDeafCount

# 2
def cheapest_path(n, costs, start):
    prices = [float('inf')] * n
    prices[start] = 0

    queue = [start]
    nxt, prv = 0, 1

    while nxt < prv:
        curr = queue[nxt]
        nxt += 1

        for c in range(n):
            if costs[curr][c] > 0:
                price = prices[curr] + costs[curr][c]

                if price < prices[c]:
                    prices[c] = price
                    queue.append(c)
                    prv += 1

    return prices

# 3
def generate_password(words):
    inp = words.copy()
    while len(inp) > 1:
        common = -1
        new_word = None

        for i in range(len(inp)):
            for j in range(len(inp)):
                if i != j and (inp[j] not in inp[i] and inp[i] not in inp[j]):
                    for k in range(min(len(inp[i]), len(inp[j])), -1, -1):
                        if inp[i].endswith(inp[j][:k]) and k > common:
                            common = k
                            new_word = (i, j)

        if new_word is None:
            break

        i, j = new_word
        inp[i] += inp[j][common:]
        inp.pop(j)

    return inp[0]
# approach discussed with Pratik Gholap

# 4
def maximumPeople(personHeight, roomHeight):
    ph = personHeight.copy()
    ph.sort()
    
    maximumNumberOfPersons, temp_j = 0, 0
    v = [False] * len(roomHeight)
    for p in range(len(ph)):
        for r in range(len(roomHeight)):
            if ph[p] <= roomHeight[r] and v[r] == False:
                v[r] = True
                if (r > 0):
                    maximumNumberOfPersons -= 1
                    v[temp_j] = False
                temp_j = r
                maximumNumberOfPersons += 1
            else:
                break
    return maximumNumberOfPersons

# 5
def smallestString(encoded: str) -> str:
        if len(encoded) == 1:
            return ""

        decoded, afl = [encoded[len(encoded) // 2]] * len(encoded), 0
        for i in range(len(encoded) // 2):
            if not afl and encoded[i] != 'a':
                decoded[i] = 'a'
                afl = 1
            else:
                decoded[i] = encoded[i]
            decoded[len(encoded) - i - 1] = encoded[i]
            
        if not afl:
            decoded[-1] = "b"
        return "".join(decoded)
# 6
def grandTour(checkpoints):
    p = [-1] * len(checkpoints)
    p[0] = 0
    
    def hfunc(p, i):
        if i == len(checkpoints):
            return checkpoints[p[i - 1]][p[0]]

        for v in range(1, len(checkpoints)):
            if checkpoints[p[i - 1]][v] and v not in p:
                p[i] = v

                if hfunc(p, i + 1):
                    return True

                p[i] = -1

        return False
    return hfunc(p, 1)