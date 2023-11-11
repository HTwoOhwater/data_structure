from DS import TreeNode


def calculator(root: TreeNode):
    if str(root.value).isdigit() or type(root.value) is float:
        return root.value
    else:
        if root.value in "+":
            return calculator(root.lchild) + calculator(root.rchild)
        elif root.value in "-":
            return calculator(root.lchild) - calculator(root.rchild)
        elif root.value in "*":
            return calculator(root.lchild) * calculator(root.rchild)
        elif root.value in "/":
            return calculator(root.lchild) / calculator(root.rchild)

while True:

    s = input("输入四则运算的算式喵：\n")
    number = 0
    HEAD = 0
    POINTER = 1
    stack = [[None, None]] # 先head，后pointer
    # 构建函数
    for i in s:

        if i in "+-*/":
            # 首先判断上一次运算
            character = TreeNode(i)
            num_temp = TreeNode(number) if type(number) is not TreeNode else number
            if stack[-1][HEAD] is None:
                stack[-1][HEAD] = character
                stack[-1][POINTER] = stack[-1][HEAD]
                stack[-1][POINTER].lchild = num_temp
                number = 0
                continue

            else:
                stack[-1][POINTER].rchild = num_temp

            if i in "*/" and stack[-1][POINTER].value in "+-*": # 乘除

                character.lchild = num_temp
                stack[-1][POINTER].rchild = character
                stack[-1][POINTER] = character

            elif i in "*/" and stack[-1][POINTER].value in "/":
                character.lchild = stack[-1][POINTER].lchild
                character.rchild = stack[-1][POINTER].rchild
                stack[-1][POINTER].lchild = character
                stack[-1][POINTER].rchild = None

            else: # 加减
                character.lchild = stack[-1][HEAD]
                stack[-1][HEAD] = character
                stack[-1][POINTER] = stack[-1][HEAD]

            number = 0

        elif i in '1234567890':
            number = 10 * number + int(i)

        elif i in "(":
            stack.append([None, None])

        elif i in ")":
            if stack[-1][POINTER] is not None:
                stack[-1][POINTER].rchild = TreeNode(number)
            number = stack[-1][HEAD] if type(number) is not TreeNode else number
            stack.pop()

        else:
            pass

    # 刚开始是括号，需要讨论
    if stack[-1][HEAD] is not None:
        stack[-1][POINTER].rchild = TreeNode(number) if type(number) is not TreeNode else number
    else:
        stack[-1][HEAD] = number
        stack[-1][POINTER] = stack[-1][HEAD]

    print(stack[-1][HEAD])
    print(calculator(stack[-1][HEAD]))
    print(stack[-1][HEAD].inorder_traversal())