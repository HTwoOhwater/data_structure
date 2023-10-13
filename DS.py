import copy


class Node:
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
        return f"[ value = {self.value} ] -> {self.next}"

    def __abs__(self):
        self.value = (self.value ** 2) * 0.5

    def __bool__(self):
        return bool(self.value)

    def __eq__(self, other):
        try:
            return self.value == other.value and self.next == other.next
        except:
            return self.value == other


    def __copy__(self):
        return Node(self.value)

    def __deepcopy__(self, memodict={}):
        if self is not None:
            p = Node(self.value)
            p.next = copy.deepcopy(self.next)
            return p
        else:
            return None

    def __len__(self):
        ls = 0
        p = self
        while p is not None:
            ls += 1
            p = p.next
        return ls

    def __getitem__(self, item):
        if item is slice:
            raise ValueError("Slice Do Not Support")
        item = self.__get__index__(item)
        p = self
        for i in range(item):
            p = p.next
        return copy.copy(p)

    def __setitem__(self, key, value):
        if key is slice:
            raise ValueError("Slice Do Not Support")
        key = self.__get__index__(key)
        p = self
        for i in range(key):
            p = p.next
        p.value = value

    def __del__(self):
        return "Target Down"

    def __lt__(self, other):
        try:
            return self.value < other.value
        except:
            return self.value < other

    def __le__(self, other):
        try:
            return self.value <= other.value
        except:
            return self.value <= other

    def __gt__(self, other):
        try:
            return self.value > other.value
        except:
            return self.value > other

    def __ge__(self, other):
        try:
            return self.value >= other.value
        except:
            return self.value >= other

    def empty(self):
        return self.next is None

    def __get__index__(self, item):
        ls = len(self)
        if item > ls or item < -ls:
            raise ValueError(f"{item} Out of the range of [{-ls + 1}, {ls - 1}]")
        elif item < 0:
            item += ls
        return item

    def seq(self, seq):
        for i in seq:
            self.push(Node(i))

    def remove(self, index):
        index = self.__get__index__(index)
        if index == 0:
            raise ValueError("Self can't be deleted!")
        index -= 1
        p = self
        for i in range(index):
            p = p.next
        q = p.next
        p.next = p.next.next
        q.next = None
        return q

    def insert(self, index, node):
        if index >= len(self):
            index = len(self) - 1
            p = self
            for i in range(index):
                p = p.next
            p.next = node
        else:
            index = self.__get__index__(index)
            if index == 0:
                raise ValueError("Self can't be inserted!")
            index -= 1
            p = self
            for i in range(index):
                p = p.next
            node.next = p.next.next
            p.next = node

    def pop(self):
        return self.remove(len(self) - 1)

    def push(self, node):
        self.insert(len(self), node)

    def clear(self):
        self.next = None


class LinkList(Node):
    def __init__(self):
        super().__init__()
        self.value = "Head Node"
        self.head = self
        self.length = 0

    def insert(self, index, node):
        node = self.__to__node__(node)
        p = self.__get__index__(index)
        p.next = node
        self.length += 1

    def remove(self, index):
        p = self.__get__index__(index)
        temp = p.next
        p.next = p.next.next
        temp.next = None
        self.length -= 1
        return temp

    def search(self, value):
        p = self.next
        for i in range(self.length):
            if value == self.value:
                return i + 1
            p = p.next
        return -1

    def __get__index__(self, index):
        p = self
        for i in range(index - 1):
            p = p.next
        return p

    def __to__node__(self, node):
        if node is not Node:
            return Node(node)


    def __be__valid__(self, index):
        if index > (- self.length - 1):
            index = (index + self.length + 1) % (self.length + 1)
        else:
            raise ValueError("index error!")

    def __len__(self):
        count = 0
        p = self.next
        while p is not None:
            p = p.next
            count += 1
        self.length = count
        return self.length






class SingleLinkList:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head
        self.length = 0
        self.iter = None

    def cat_list(self, ls):
        self.tail.next = ls.head.next
        self.tail = ls.tail

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
        while count != index - 1:
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
            count += 1
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
        self.top = Node(0)
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
