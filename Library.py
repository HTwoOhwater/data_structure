from DS import *


class Library(LinkList):
    def __repr__(self):
        def __node__(node):
            if node is None:
                return "End Of Data\n"
            return f"{node.value[0]:20} {node.value[1]:{chr(12288)}<15} {node.value[2]:10}\n{__node__(node.next)}"

        return f"{'ISBN':20} {'书名':{chr(12288)}<15} {'价格':10}\n{__node__(self.next)}"

    def count(self):
        return f"目前图书馆书本数量为:{self.length}"

    def search(self, value, key):
        value = str(value)
        count = 0
        index = []
        p = self.next
        for i in range(self.length):
            if value == p.value[key]:
                print(f"ISBN：{p.value[0]:20} 书名：{p.value[1]:{chr(12288)}<15} 价格：{p.value[2]:10}")
                count += 1
                index.append(i + 1)
            p = p.next
        if count > 0:
            print(f"找到了{count}条数据\n")
            return index
        else:
            print("未找到相关数据！\n")
            return None

    def modify(self, index, value, key):
        p = self.__get__index__(index)
        p.value[key] = str(value)

    def sort(self, key):
        for i in range(self.length):
            p = self.next
            for i in range(self.length - 1):
                if eval(p.value[key]) > eval(p.next.value[key]):
                    p.value, p.next.value = p.next.value, p.value
                p = p.next


data = Library()
with open(file="./data.txt", mode="r", encoding="UTF-8") as f:
    f.readline().split()
    for i in f.readlines():
        temp = i.split()
        data.insert(data.length + 1, temp)

print(data)
data.search(32, 2)
