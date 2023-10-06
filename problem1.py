from data_structure import *

l1 = input("输入链表A").split()
l2 = input("输入链表B").split()
sl1 = SingleLinkList()
sl2 = SingleLinkList()

for i in l1:
    sl1.cat_node(Node(eval(i)))
for i in l2:
    sl2.cat_node(Node(eval(i)))

sl1.show_all()
sl2.show_all()

p = sl1.head.next
q = sl2.head.next

sl = SingleLinkList()

while p is not None or q is not None:
    if p is None:
        while q is not None:
            t = q.next
            sl.cat_node(q)
            q = t
        break
    elif q is None:
        while p is not None:
            t = p.next
            sl.cat_node(p)
            p = t
        break
    else:
        if p.value > q.value:
            t = q.next
            sl.cat_node(q)
            q = t
        elif p.value <= q.value:
            t = p.next
            sl.cat_node(p)
            p = t


sl.be_set()

sl.show_all()
