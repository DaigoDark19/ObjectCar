
#EJEMPLO 1:
# class TreeNode():
#     def __init__(
#         self,
#         data,
#         left: 'TreeNode' = None,
#         right: 'TreeNode' = None
#     ) -> None:

#         self.data = data
#         self.left: TreeNode = left
#         self.right: TreeNode = right

#     def insert_left(self, data):
#         self.left = TreeNode(data)
#         return self.left

#     def insert_right(self, data):
#         self.right = TreeNode(data)
#         return self.right


# class BinaryTree():
#     def __init__(self) -> None:
#         self.root: TreeNode = None
#         self.size = 0

#     def inser_node(self, data):
#         if self.root is None:
#             self.root = TreeNode(data)
#         else:
#             self._insert_node(self.root, data)

#     def _insert_node(self, node, data):
#         ...


# binary_tree = BinaryTree()

# root = TreeNode(1)
# binary_tree.root = root

# # approx el 50% de los nodos van a la izquierda y el otro 50% a la derecha

# root.right = TreeNode(3)
# root.right.right = TreeNode(7)
# root.right.right.right = TreeNode(9)
# root.right.right.right.right = TreeNode(11)
# root.right.right.right.right.right = TreeNode(13)


# #    3
# #   1 11
# #     7 15

# #    11
# #  3 7 15


# # EJEMPLO 2:
# class nodo():
#     def __init__(self, data) -> None:
#         self.data = data
#         self.left = None
#         self.right = None


# class tree():
#     def __init__(self) -> None:
#         self.root = None

#     def vacio(self) -> bool:
#         return self.root is None

#     def verificar_pos(self, data):
#         aux: nodo = self.root
#         while aux is not None:
#             temp: nodo = aux
#             if data <= aux.data:
#                 aux = aux.left
#             else:
#                 aux = aux.right
#         return temp

#     def agregar(self, data):
#         if self.vacio():
#             self.root = nodo(data)
#         else:
#             ultima_pos = self.verificar_pos(data)
#             if data <= ultima_pos.data:
#                 ultima_pos.left = nodo(data)
#             else:
#                 ultima_pos.right = nodo(data)

#     def recorrido_uno(self, node):
#         if node:
#             self.recorrido_uno(node.left)
#             print(node.data)
#             self.recorrido_uno(node.right)


# prueba = tree()
# prueba.agregar(2)
# prueba.agregar(1)
# prueba.agregar(8)
# prueba.agregar(6)

# prueba.recorrido_uno(prueba.root)


class nodo():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class tree():
    def __init__(self) -> None:
        self.root = None

    def vacio(self) -> bool:
        return self.root is None

    def verificar_pos(self, data):
        aux: nodo = self.root
        while aux is not None:
            temp: nodo = aux
            if data <= aux.data:
                aux = aux.left
            else:
                aux = aux.right
        return temp

    def agregar(self, array):
        for n in array:
            if self.vacio():
                self.root = nodo(n)
            else:
                ultima_pos = self.verificar_pos(n)
                if n <= ultima_pos.data:
                    ultima_pos.left = nodo(n)
                else:
                    ultima_pos.right = nodo(n)

    def recorrido_uno(self, node):
        if node:
            self.recorrido_uno(node.left)
            print(node.data)
            self.recorrido_uno(node.right)


prueba = tree()
prueba.agregar([5, 3, 2, 9, 7])
prueba.recorrido_uno(prueba.root)
