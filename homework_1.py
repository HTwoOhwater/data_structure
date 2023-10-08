# 作业内容为：合并有顺序的链表，且不能重复。
from DS import *
while True:
    # 链表头
    ll1 = Node(None)
    ll2 = Node(None)
    # 展示以下列表转化功能
    ls1 = []
    ls2 = []
    # 输入
    arr1 = input("输入链表1\n").split()
    arr2 = input("输入链表2\n").split()
    # 字符串转化为数组
    for i in arr1:
        ls1.append(eval(i))
    for i in arr2:
        ls2.append(eval(i))
    # 防止非法输入，提前整理
    ls1.sort()
    ls2.sort()
    # 列表链表化
    ll1.seq(ls1)
    ll2.seq(ls2)
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
    standard = None
    # 找到最小的那一个当作标准
    if ll1.next.value > ll2.next.value:
        standard = ll2.next
        p2 = p2.next
    else:
        standard = ll1.next
        p1 = p1.next
    # 建立头指针
    head = standard
    # 标准初始化
    standard.next = None
    # 判断过程
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
    # 一个链表为空了之后，另一个就可以直接合并上去
    p = None
    if p1 is None:
        while p2.value <= standard.value:
            p2 = p2.next
            if p2 is None:
                break
        p = p2
        while p is not None:
            if p.next is None:
                break
            while p.next.value == p.value:
                p.next = p.next.next
                if p.next is None:
                    break
            p = p.next
            if p is None:
                break
        standard.push(p2)
    elif p2 is None:
        while p1.value <= standard.value:
            p1 = p1.next
            if p1 is None:
                break
        p = p1
        while p is not None:
            if p.next is None:
                break
            while p.next.value == p.value:
                p.next = p.next.next
                if p.next is None:
                    break
            p = p.next
            if p is None:
                break
        standard.push(p1)
    # 打印结果
    print(head)
