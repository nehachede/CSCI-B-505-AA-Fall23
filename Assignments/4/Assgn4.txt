def MinimumExpenditure(AppleTreePrice):
    dp = [list(AppleTreePrice[0])]
    
    for i in range(1, len(AppleTreePrice)):
        dp.append([0, 0, 0])
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + AppleTreePrice[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + AppleTreePrice[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + AppleTreePrice[i][2]

    return min(dp[-1])

def alignments(A, B):
    
    dp_mat = [[1]*(B+1) for _ in range(A+1)]
    for i in range(1, A+1):
        for j in range(1, B+1):
            dp_mat[i][j] = dp_mat[i-1][j] + dp_mat[i][j-1] + dp_mat[i-1][j-1]
    
    return dp_mat[A][B]

def smallestMissingNumber(streetNumbers):
    number = 0
    r = len(streetNumbers) - 1
    
    while number <= (r):
        mid = number + (r - number) //2
        
        if streetNumbers[mid] == mid:
            number = mid + 1
        else:
            r = mid -1
    return number

def solution_inheritance(num_items, num_boxes, children):
    if children > num_boxes or children <= 0 or num_boxes <= 0:
        return -1

    l, r = max(num_items), sum(num_items)

    while l < r:
        mid = (l + r) // 2
        child = 1
        add = 0
        
        for i in num_items:
            if i > mid:
                child = children + 1
                break

            if add + i <= mid:
                add += i
            else:
                child += 1
                add = i

        if child <= children:
            r = mid
        else:
            l = mid + 1
    return l

def place_max_speedbump(len_road, bump_int1, bump_int2, bump_int3):
    max_bumps = [0] * (len_road + 1)

    for i in range(1, len_road + 1):
        max_bumps[i] = -1

        if i >= bump_int1 and max_bumps[i - bump_int1] >= 0:
            max_bumps[i] = max(max_bumps[i], max_bumps[i - bump_int1] + 1)
        if i >= bump_int2 and max_bumps[i - bump_int2] >= 0:
            max_bumps[i] = max(max_bumps[i], max_bumps[i - bump_int2] + 1)
        if i >= bump_int3 and max_bumps[i - bump_int3] >= 0:
            max_bumps[i] = max(max_bumps[i], max_bumps[i - bump_int3] + 1)

    if max_bumps[len_road] >= 0:
        return max_bumps[len_road]
    else:
        return 0


def find_path(stone_inscription_list):
    n = len(stone_inscription_list)
    
    part = [float('inf')] * n
    part[0] = 0

    for i in range(n):
        for j in range(i + 1, min(i + stone_inscription_list[i] + 1, n)):
            if part[i] + 1 < part[j]:
                part[j] = part[i] + 1
    
    return part[-1]

def decode_cryptic_message(lists):
  if len(lists) <= 1:
    return lists[0]

  mid = len(lists) // 2
  l = decode_cryptic_message(lists[:mid])
  r = decode_cryptic_message(lists[mid:])

  arranged_numbers = []
  i = 0
  j = 0
  while i < len(l) and j < len(r):
    if l[i] < r[j]:
      arranged_numbers.append(l[i])
      i += 1
    else:
      arranged_numbers.append(r[j])
      j += 1

  arranged_numbers += l[i:]
  arranged_numbers += r[j:]

  return arranged_numbers