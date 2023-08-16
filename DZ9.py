
import random

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        if self.head is None:
            print("Список пуст!")
            return
        else:
            cur_node = self.head
            while cur_node is not None:
                print(cur_node.value, end = " ")
                cur_node = cur_node.next
                
    def insert_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def rand_list(self):
        add = random.sample(range(1, 16), 15)
        for i in add:
            ll.insert_start(i)
        return
        
    def sort(self):
        end = None
        while end != self.head:
            cur_node = self.head
            while cur_node.next != end:
                node = cur_node.next
                if cur_node.value > node.value:
                    cur_node.value, node.value = node.value, cur_node.value
                cur_node = cur_node.next
            end = cur_node        
    
    def spis(self):
        lst = []
        cur_node = self.head
        while cur_node is not None:
            lst.append(cur_node.value)
            cur_node = cur_node.next
        return lst
        
    def list_for_tree(self, st, end):
        newlst = []
        if st > end:
            return []
        mid = int(st + (end - st) / 2)
        root = [mid]
        left = ll.list_for_tree(st, mid-1)
        right = ll.list_for_tree(mid+1, end)
        
        newlst = root + left+ right
        return newlst
    
    # DEREVO

class NOde():
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None
        self.parent = None

class BinTree:
    def __init__(self):
        self.root = NOde()
        
    def tree_from(self):
        cher2 = ll.list_for_tree(1, 15)
        for i in cher2:
            bst.add(i)
        return    

    def add(self, value):
        if self.root.value is None:
            self.root.value = value
            return
        self.add_data(self.root, value)

    def add_data(self, cn, value):
        if cn.value > value:
            if cn.left is None:
                cn.left = NOde()
                cn.left.value = value
                cn.left.parent = cn
            else:
                self.add_data(cn.left, value)
        else:
            if cn.right is None:
                cn.right = NOde()
                cn.right.value = value
                cn.right.parent = cn
            else:
                self.add_data(cn.right, value)

    def find(self, value):
        if self.root.value is None:
            return False
        if self.root.value == value:
            return True
        node = self.find_node(self.root, value)
        if node is None:
            return False
        return True

    def find_node(self, cn, value):
        if cn is None:
            return None
        if cn.value == value:
            return cn

        if cn.value > value:
            res = self.find_node(cn.left, value)
            return res
        else:
            res = self.find_node(cn.right, value)
            return res

    def find_min(self):
        node = self.find_min_node(self.root)
        return node.value

    def find_min_node(self, cn):
        if cn.left is None:
            return cn

        node = self.find_min_node(cn.left)
        return node

    def find_max(self):
        node = self.find_max_node(self.root)
        return node.value

    def find_max_node(self, cn):
        if cn.right is None:
            return cn

        node = self.find_max_node(cn.right)
        return node

    def delete(self, value):
        if self.root.left is None and self.root.right is None and self.root.value == value:
            self.root.value = None
            return

        if self.root.left is not None and self.root.right is None and self.root.value == value:
            self.root = self.root.left
            self.root.parent = None
            return

        if self.root.left is None and self.root.right is not None and self.root.value == value:
            self.root = self.root.right
            self.root.parent = None
            return
        
        if self.root.left is not None and self.root.right is not None and self.root.value == value:
            min_node_of_right = self.find_min_node(self.root.right)
            self.root = min_node_of_right
            min_node_of_right = None
            return

        node = self.find_node(self.root, value)
        if node is None:
            raise Exception("No")
        self.delete_data(node)


    def delete_data(self, node):
        if node.left is None and node.right is None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
            return

        if node.left is not None and node.right is None:
            if node.parent.left == node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
            return

        if node.left is None and node.right is not None:
            if node.parent.left == node:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            return

        if node.left is not None and node.right is not None:
            min_node_of_right = self.find_min_node(node.right)
            min_node_of_right.left = node.left
            if node.parent == node:
                node.parent.left = min_node_of_right
            else:
                node.parent = min_node_of_right
            return

        raise Exception("WTF")


           
ll = LinkedList()

ll.rand_list()

ll.print_list()

ll.sort()

print()

ll.print_list()

print()

ll.spis()

cher = ll.spis()
print(cher)

bst = BinTree()

cher2 = ll.list_for_tree(1, 15)
print(cher2)

bst.tree_from()

print(bst.find_min(), bst.find_max())

bst.delete(8)

print(bst.find(8))

print(bst.find(9))

bst.printTree(bst)
