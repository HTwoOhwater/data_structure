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
        if index >= 1 or -self.length <= index <= -1:
            index = (abs(index) - 1) % self.length
            return index
        elif index is None:
            raise ValueError("Head Node CANNOT Be Operated!")
        else:
            raise ValueError("Index Error!")


    def __len__(self):
        count = 0
        p = self.next
        while p is not None:
            p = p.next
            count += 1
        self.length = count
        return self.length


class Stack(LinkList):
    # 栈的数据结构
    def __init__(self):
        self.value = "Top Of Stack"
        self.length = 0
        self.next = None

    def push(self, node):
        node = self.__to__node__(node)
        node.next = self.next
        self.next = node
        self.length += 1

    def pop(self):
        temp = self.next
        self.next = self.next.next
        temp.next = None
        self.length -= 1
        return temp

    def peek(self):
        if self.length:
            return self.next.value
        else:
            return self.value


class Queue(LinkList):
    def __init__(self):
        self.value = "Head Of Queue"
        self.length = 0
        self.next = None
        self._rear = self

    def push(self, node):
        node = self.__to__node__(node)
        self._rear.next = node
        self._rear = node
        self.length += 1

    def pop(self):
        temp = self.next
        self.next = self.next.next
        temp.next = None
        self.length -= 1
        return temp

