class Node:
    def __init__(self, data: int, next: 'Node' = None) -> None:

        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)


prev: Node = None
head: Node = None
current_node: Node = None

for i in range(1, 11):
    current_node = Node(data=i)

    if not head:
        head = current_node

    if prev:
        prev.next = current_node

    prev = current_node

current_node = head
# for i in range(10):
#     print(current_node)
#     current_node = current_node.next

matrix = [[0 for i in range(10)] for _ in range(10)]
for i in range(len(matrix)):
    print(matrix[i])


node1 = Node(data=1)

node2 = Node(data=2)

node1.next = node2

current_node = head
for i in range(10):
    print(current_node)
    current_node = current_node.next


"""

[node1, 1, 1, node2, 0, 1, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0, 0, node6]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, node3, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 0, node5, 0]
[node4, 0, 0, 0, 0, 0, 0, 0, 0, 0]

"""


class Node():
    def __init__(self, data: int, next: 'Node' = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)


class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data: int):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self) -> str:
        current_node = self.head
        result = []
        while current_node:
            result.append(str(current_node))
            current_node = current_node.next
        return ' -> '.join(result)


# Big O notation
# Time, Space
# O(1), O(1)

dict1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

value = dict1['a']  # O(1)


def sum(a: int, b: int) -> int:
    return a + b  # O(1) Time, O(1) Space

# O(n) -> time


def sum_list(list1: list[int]) -> int:
    # O(n) -> time

    result = 0
    for i in list1:
        result += i
    return result


def sum_list2(list1: list[int]) -> int:
    # O(n**2) -> time

    result = 0
    for i in list1:
        for j in list1:
            result += i + j

# x = 2
# x = 3, x = 4, x = 5, x = 6, x = 7, x = 8, x = 9, x = 10
# x**2 = 4, 9, 16, 25, 36, 49, 64, 81, 100
# log(x) = 1, 1.58, 2, 2.32, 2.58, 2.81, 3, 3.16, 3.32

# O(log(n)) -> time


l = [1, 5, 8, 12, 16, 200, 500, 900, 10000]

obj = 500
for i in l:
    if i == obj:
        print('Found')
        break

# binary search


car_list = [1000]
cars_that_move = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Space O(n)


l = [i for i in range(10**10)]  # O(n)

LinkedList1 => 'cantidad de carros'
LinkedList2 => 'cantidad de carrros que se movieron'




