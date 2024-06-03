class Node():
    def __init__(self, data: object, next: 'Node' = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)


class LinkedList():
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete(self, data):
        if self.size <= 0:
            raise ValueError("La lista esta vacia")

        current = self.head

        if current.data == data:
            self.head = current.next
            return

        while current.next.data != data:
            if current.next is None:
                raise ValueError("el siguiente nodo no hay nada")
            current = current.next
        delete_node = current.next
        current.next = delete_node.next
        self.size -= 1

    def delete_all(self):
        self.head = None
        self.tail = None
        self.size = 0

    def len(self):
        return self.size

    def __str__(self) -> str:
        current_node = self.head
        result = []
        while current_node:
            result.append(str(current_node))
            current_node = current_node.next
        return ' -> '.join(result)


# mi_list = LinkedList()

# mi_list.append(2)
# mi_list.append(7)
# mi_list.append(1)
# mi_list.append(5)
# mi_list.append(100)
# print(mi_list)

# mi_list.delete(7)
# mi_list.delete(2)
# mi_list.delete(100)
# mi_list.delete(5)
# print(mi_list)
