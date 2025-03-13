# Question 3
def minimum_balls(c1, c2, c3, c4, c5, p):
    balls_nminus1 = sum(min(c, p-1) for c in [c1, c2, c3, c4, c5])
    total_balls_taken_out = balls_nminus1 + 1
    return total_balls_taken_out

# print(minimum_balls(3, 4, 3, 9, 23, 1));
# print(minimum_balls(3, 4, 3, 9, 23, 2));
# print(minimum_balls(20, 20, 20, 20, 20, 3));

# Question 4
def longestBlues(tiles, k) -> int:
    number_of_tiles = blue_n = j = 0
    
    for i in range(len(tiles)):
        if tiles[i] == "blue":
            blue_n += 1
        if i - j + 1 - blue_n > k:
            if tiles[j] == "blue":
                blue_n -= 1
            j += 1
        number_of_tiles = max(number_of_tiles, i - j + 1)
    return number_of_tiles

# print(longestBlues(["blue","blue","blue","pink","pink","pink","blue","blue","blue","blue","pink"], 2))
# print(longestBlues(["pink","pink","blue","blue","pink","blue","blue","pink"], 1))

#Question 5
import re

def CandiesLog(s):
    pattern = r'([a-z])(\d+)'
    matches = re.findall(pattern, s)
    
    kids = len(matches)
    total_candies = sum(int(count) for _, count in matches)
    
    candy = {}
    for flavour, count in matches:
        candy[flavour] = candy.get(flavour, 0) + int(count)
        
    sorted_str = ''.join(f'{flavour}{count}' for flavour, count in sorted(candy.items()))

    res = f'K{kids}T{total_candies}{sorted_str}'
    return res

# print(CandiesLog('a1a5b2c3'))
# print(CandiesLog('c18d4d13b6a14c5'))
# print(CandiesLog('a13z70p2a9f6'))

# Question 6
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class HeimdallQuest:
    def reverse_k_steps(self, head, k):
        if not head or k <= 1:
            return head

        # Count the number of nodes in the Linked List
        def count_nodes(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        num_nodes = count_nodes(head)

        if num_nodes < k:
            # return the original list
            return head

        prev = None
        current = head
        for _ in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        head.next = self.reverse_k_steps(current, k)

        return prev

    def get_linked_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def create_linked_list(self, lst):
        if not lst:
            return None

        head = Node(lst[0])
        current = head
        for value in lst[1:]:
            current.next = Node(value)
            current = current.next
        return head

# hq = HeimdallQuest()
# head = hq.create_linked_list([1, 2, 3, 4, 5])
# new_head = hq.reverse_k_steps(head, 2)
# print(hq.get_linked_list(new_head))

# head = hq.create_linked_list([76,23,22,65,34])
# new_head = hq.reverse_k_steps(head, 6)
# print(hq.get_linked_list(new_head))

# head = hq.create_linked_list([1, 2, 3, 4, 5])
# new_head = hq.reverse_k_steps(head, 3)
# print(hq.get_linked_list(new_head))