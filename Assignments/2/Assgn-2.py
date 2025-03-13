# question 1
def amountPoliceGets(people):
    p = people

    money_stack = []
    
    if not p:
        return 0
    
    i = 0
    while p[i][0] != 1 and p[i][0] != 0:
      i += 1

    p = p[i:]
    
    j = len(p) - 1
    while p[j][0] != -1 and p[j][0] != 0:
      j -= 1

    p = p[:j + 1]
    
    money_collected = left = right = i = 0
    
    for direction, amount in p:
        if direction == 0:
            i += 1
            continue
            
        if direction == -1 or direction == 1:
            money_stack.append(amount)
            if direction == 1:
                left+=1;
            if direction == -1:
                right+=1;
        i += 1
    
    while money_stack:
        money_collected += money_stack.pop(0)
    
    if (left == len(people) or right == len(people)):
        return 0
    else:
        return money_collected

# print(amountPoliceGets([[1, 3], [1, 10], [1, 4], [1, 7], [1, 12], [1, 6]]))
# print(amountPoliceGets([[1,3] , [-1,10], [1,4] , [0,7] , [-1, 12] , [-1,6]]))
# print(amountPoliceGets([[0,1],[0,10],[1,1],[0,7],[0,12],[1,1],[-1,1],[-1,1],[1,1],[0,1],[-1,1],[-1,1],
#                         [1,1],[0,1],[1,1],[0,1],[0,1],[1,1],[-1,1],[1,1],[1,1],[1,1],[1,1],[-1,1],[-1,1],[1,1],
#                         [1,1],[-1,1],[0,1],[0,1],[1,1],[1,1]]))
# print(amountPoliceGets([[1,3],[0,10],[0,4],[0,7],[0,12],[0,6]]))

# question 2
import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.down = None

class SkipList:
    def __init__(self):
        self.head = Node(float('-inf'))
        self.levels = 1
        self.max_levels = 32
        self.prob = 0.5
        self.size = 0
        
    def search(self, target: int) -> bool:
        current = self.head

        while current:
            if current.next and current.next.val < target:
                current = current.next
            elif current.next and current.next.val == target:
                return True
            elif current.down:
                current = current.down
            else:
                break
            
        return False

    def insert(self, num: int) -> None:
        update = [None] * self.max_levels
        current = self.head
        
        for level in range(self.levels - 1, -1, -1):
            while current.next and current.next.val < num:
                current = current.next
            update[level] = current
            if current.down:
                current = current.down

        new_level = 1
        while random.random() < self.prob and new_level < self.max_levels:
            new_level += 1

        if new_level > self.levels:
            for i in range(self.levels, new_level):
                update[i] = self.head
            self.levels = new_level

        new_node = Node(num)
        for i in range(new_level):
            new_node.next = update[i].next
            update[i].next = new_node
            new_node = Node(num)
            if i < new_level - 1:
                new_node.down = update[i].next

        self.size += 1
        
# Example:
sl = SkipList()
print(sl.insert(1)) # None
print(sl.insert(2)) # None
print(sl.insert(3)) # None
print(sl.search(4)) # False
print(sl.insert(4)) # None
print(sl.search(4)) # True
print(sl.search(1)) # True
    
# question 3
class Queue:
    def __init__(self):
        self.DEFAULT_SIZE = 10
        self.queue = [-1] * self.DEFAULT_SIZE
        self.front = self.rear = self.size = 0

    def enque(self, item):
        if self.size == self.DEFAULT_SIZE:
            return False
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.DEFAULT_SIZE
            self.size += 1
            return True

    def deque(self):
        if self.size == 0:
            return -1
        else:
            item = self.queue[self.front]
            self.front = (self.front + 1) % self.DEFAULT_SIZE
            self.size -= 1
            return item


# queue = Queue()
# print(queue.enque(1))
# print(queue.enque(2))
# print(queue.enque(3))

# queue = Queue()
# print(queue.deque())
# print(queue.enque(1))
# print(queue.enque(2))
# print(queue.enque(3))
# print(queue.deque())
# print(queue.deque())
# print(queue.deque())
# print(queue.deque())

# question 4
def isItPossible(initial, final):
    exp = final[::-1]
        
    if initial == final or initial == exp:
         return True
    
    temp = []
    index = 0
    
    for i in initial:
        
        if i == exp[index]:
            index+=1
        else:
            temp.append(i);
        
        while temp and temp[-1] == exp[index]:
            temp.pop()
            index += 1
        
    if not temp :
        return True
    else:
        return False
    
# print(isItPossible(['Red', 'Blue', 'Green', 'Yellow', 'Orange'], 
#                     ['Yellow', 'Orange', 'Green', 'Blue', 'Red']))
# print(isItPossible(['Red', 'Blue', 'Green', 'Yellow', 'Orange'], 
#                     ['Yellow', 'Green', 'Orange', 'Red', 'Blue']))
# print(isItPossible(["Red","Blue","Green","Yellow","Orange","Violet","Brown"], 
#                     ["Green","Yellow","Brown","Orange","Violet","Blue","Red"]))