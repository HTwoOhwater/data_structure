from DS import *


def helper(root, s: str):
    if root is None:
        pass
    else:
        s += f"{root.value}->"
        helper(root.lchild, s)
        print(f"路径：{s[:-2]} 长度：{s[:-2].count('->')}")
        helper(root.rchild, s)


# 这是第二小题喵
tree1 = TreeNode()
tree1.generate([1, 2, 3])
tree2 = TreeNode()
tree2.generate([i for i in range(7)])
print(tree2 == tree1)
print(tree2)
helper(tree2, "")
# 这是第八小题喵

