# 作业内容为：合并有顺序的链表，且不能重复。
from DS import *

# 链表头
ll1 = Node(None)
ll2 = Node(None)
# 展示以下列表转化功能
# 输入
arr1 = input("输入链表1\n").split()
arr2 = input("输入链表2\n").split()
# 字符串转化为数组
ll1.seq([eval(i) for i in arr1])
ll2.seq([eval(i) for i in arr2])
# 一个为空，直接答案就出来了
if ll1.next is None:
    print(ll2.next)
    quit(0)
elif ll2.next is None:
    print(ll1.next)
    quit(0)
# 两个指针
p1 = ll1.next
p2 = ll2.next
# 先合并
head = min(p1, p2)
rear = head
while isinstance(p1, Node) and isinstance(p2, Node):
    temp = min(p1, p2)
    if temp == p1:
        p1 = p1.next
        temp.next = None
    else:
        p2 = p2.next
        temp.next = None
    rear.next = temp
    rear = rear.next
if p1 is None:
    head.push(p2)
else:
    head.push(p1)
# 再去除重复
p = head
while p is not None and p.next is not None:
    while p.value == p.next.value:
        p.next = p.next.next
        if p.next is None:
            break
    p = p.next

# 打印结果
print(head)
