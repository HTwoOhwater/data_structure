# 作业内容为：合并有顺序的链表，且不能重复。
from DS import *


ll1 = Node(None)
ll2 = Node(None)

ls1 = []
ls2 = []

arr1 = input("输入链表1").split()
arr2 = input("输入链表2").split()

for i in arr1:
    ls1.append(eval(i))
for i in arr2:
    ls2.append(eval(i))

ls1.sort()
ls2.sort()

ll1.seq(ls1)
ll2.seq(ls2)

if ll1.next is None:
    print(ll2)
    quit(0)
elif ll2.next is None:
    print(ll1)
    quit(0)

p1 = ll1.next
p2 = ll2.next
standard = None

if ll1.next.value > ll2.next.value:
    standard = ll2.next
    p2 = p2.next
else:
    standard = ll1.next
    p1 = p1.next

head = standard

standard.next = None

while p1 is not None and p2 is not None:
    if p1.value < p2.value:
        if p1.value > standard.value:
            temp = p1
            p1 = p1.next
            temp.next = None
            head.push(temp)
            standard = standard.next
        else:
            p1 = p1.next
    else:
        if p2.value > standard.value:
            temp = p2
            p2 = p2.next
            temp.next = None
            head.push(temp)
            standard = standard.next
        else:
            p2 = p2.next

if p1 is None:
    while p2.value <= standard.value:
        p2 = p2.next
        if p2 is None:
            break
    standard.push(p2)
elif p2 is None:
    while p1.value <= standard.value:
        p1 = p1.next
        if p1 is None:
            break
    standard.push(p1)

print(head)
