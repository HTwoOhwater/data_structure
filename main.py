from data_structure import *

l = SingleLinkList()
for i in range(5):
    l.cat_node(Node(i))
i = iter(l)
for j in i:
    print(j)
