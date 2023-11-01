from DS import TreeNode


def calculator(root: TreeNode): # 1-2*4/6+5
    if str(root.value).isdigit() or type(root.value) is float:
        return root.value
    else:
        if root.value in "+":
            return calculator(root.lchild) + calculator(root.rchild)
        elif root.value in "-":
            return calculator(root.lchild) - calculator(root.rchild)
        elif root.value in "*":
            return calculator(root.lchild) * calculator(root.rchild)
        else:
            return calculator(root.lchild) * calculator(root.rchild)



s = input("输入四则运算的算式喵：\n")
head = None
number = 0
pointer = None
for i in s:
    if i in "+-":
        character = TreeNode(i)
        if pointer is not None:
            temp = TreeNode(1 / number) if pointer.value in "/" else TreeNode(number)
            pointer.rchild = temp
            character.lchild = head
            head = character
        elif head is not None:
            temp = TreeNode(number)
            if head.value in "*/":
                pointer.rchild = temp
                character.lchild = head
                head = character
            else:
                head.rchild = temp
                character.lchild = head
                head = character
        else:
            temp = TreeNode(number)
            head = character
            head.lchild = temp
        pointer = None
        number = 0

    elif i in "/*":

        character = TreeNode(i)
        if pointer is not None:
            temp = TreeNode(1 / number) if pointer.value in "/" else TreeNode(number)
        else:
            temp = TreeNode(number)
        if head is not None:
            if pointer is not None:
                pointer.rchild = character
                pointer = pointer.rchild
                pointer.lchild = temp
            elif head.value in "*/":
                 pointer.rchild = character
                 pointer = pointer.rchild
                 pointer.lchild = temp
            else:
                head.rchild = character
                pointer = head.rchild
                pointer.lchild = temp

        else:
            head = character
            head.lchild = temp
            pointer = head

        number = 0

    elif i in "1234567890":
        number = 10 * number + int(i)

    else:
        pass
if pointer is None:
    head.rchild = TreeNode(number)
else:
    pointer.rchild = TreeNode(1 / number) if pointer.value in "/" else TreeNode(number)



print(head, calculator(head))
