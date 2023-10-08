# 想加上python倒着的用法

class Node:
    # 节点类就只有两个属性——值和引用
    def __init__(self, value=0):
        self.value = value
        self.next = None

    def __add__(self, other):
        self.value += other
        return self.value

    def __radd__(self, other):
        self.value += other
        return self.value

    def __repr__(self):
        return f"[ value = {self.value} ] next -> {self.next}"


class SingleLinkList:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self.length = 0
        self.iter = None

    def cat_list(self, l):
        self.tail.next = l.head.next
        self.tail = l.tail

    def cat_node(self, node: Node):
        if self.head.next is None and self.tail is None:
            self.head.next = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.tail.next = None
        self.length += 1

    def be_set(self):
        p = self.head.next
        while p.next is not None:
            while p.value == p.next.value:
                p.next = p.next.next
                if p.next is None:
                    break
            if p.next is None:
                break
            p = p.next



    def show_all(self):
        print("head->", end="")
        p = self.head.next
        while p is not None:
            print("{}->".format(p.value), end="")
            p = p.next
        print(None)

    def get(self, index: int):
        if index < 1 or index > self.length:
            raise Exception("输入了一个超出链表长度范围的值，链表节点:{}-{}".format(1, self.length))
        p = self.head
        for i in range(index):
            p = p.next
        return p.value

    def delete(self, index: int):
        if index < 1 or index > self.length:
            raise Exception("输入了一个超出链表长度范围的值，链表节点:{}-{}".format(1, self.length))
        p = self.head.next
        count = 1
        if index == 1:
            self.head.next = self.head.next.next
            return None
        while count != index - 1 :
            p = p.next
            count += 1
        temp = p.next
        p.next = p.next.next
        del(temp)

    def search(self, sign: int):
        p = self.head.next
        count = 1
        while p is not None:
            if p.value == sign:
                return count
            count+=1
            p = p.next
        return -1

    def insert(self, index: int, node: Node):
        if index < 1 or index > self.length:
            raise Exception("输入了一个超出链表长度范围的值，链表节点:{}-{}".format(1, self.length))
        p = self.head.next
        count = 1
        if index == 1:
            node.next = self.head.next
            self.head.next = node
            return None
        while count != index - 1:
            count += 1
            p = p.next
        temp_node = p.next
        node.next = temp_node
        p.next = node

    def __iter__(self):
        self.iter = self.head
        return self

    def __next__(self):
        if self.iter.next is not None:
            self.iter = self.iter.next
            return self.iter
        else:
            raise StopIteration


    def next(self, sign: int):
        index = self.search(sign) + 1
        return self.get(index)


class Stack:
    # 栈的数据结构
    def __init__(self):
        # 定义栈顶，栈底作为头节点，栈顶作为指针
        self.top = Node(None)
        self.length = 0

    def show_stack(self):
        print("top >> ", end="")
        p = self.top
        while p.next is not None:
            p = p.next
            print("{} >> ".format(p.value), end="")
        print("bottom")

    def push(self, node: Node):
        # 入栈喵
        node.next = self.top.next
        self.top.next = node

    def pop(self):
        self.top.next = self.top.next.next