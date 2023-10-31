from DS import *

s = input()
length = len(s)
chars = list(set(s))
weights = []
for char in chars:
    weights.append(s.count(char))
result = [[chars[i], weights[i]] for i in range(len(chars))]


def huffman(content):
    content = [TreeNode(i) for i in content]
    content = sorted(content, key=lambda x: x.value[1])
    while len(content) > 1:
        temp = TreeNode([None, None])
        temp.lchild = content.pop(0)
        temp.rchild = content.pop(0)
        temp.value[1] = temp.lchild.value[1] + temp.rchild.value[1]
        content.append(temp)
        content = sorted(content, key=lambda x: x.value[1])
    return content[0]


print(huffman(result))
