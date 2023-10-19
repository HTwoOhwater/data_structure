def cal(s: str) -> int:
        stack = []
        sign = 1
        num = 0
        result = 0
        status = False
        cal = True
        for c in s:
            if c == " ":
                pass
            elif c in "1234567890":
                num = num * 10 + int(c)
            elif c in "+-":
                if status:
                    if cal:
                        stack.append(stack.pop() * num)
                    else:
                        t = stack[-1]
                        stack.append(abs(stack.pop()) // num * abs(t)//t)
                    status = False
                else:
                    stack.append(num * sign)
                num = 0
                sign = 1 if c == "+" else -1
            elif c in "*/":
                if status:
                    if cal:
                        stack.append((stack.pop()) * num)
                        cal = True
                    else:
                        t = stack[-1]
                        stack.append(abs(stack.pop()) // num * abs(t)//t)
                        cal = False
                else:
                    stack.append(num * sign)
                    status = True
                cal = True if c in "*" else False
                num = 0
                sign = 1
        if status == True:
            if cal:
                stack.append(stack.pop() * num)
            else:
                t = stack[-1]
                stack.append(abs(stack.pop()) // num * abs(t)//t)
        else:
            stack.append(num * sign)
        
        for n in stack:
            result += n
            
        return result


def calculate(s: str) -> float:  # 永远以加法为中心
    cast = dict({"+": 1, "-": -1})
    stack = [0]
    num = 0.
    sign = 1
    def mul_div():
        nonlocal num
        nonlocal sign
        if str(stack[-1]) in "*/":
            char = stack.pop()
            if char in "*":
                num = stack.pop() * num
            else:
                num = stack.pop() / num
            sign = 1

    for c in s:  # 检测是否为数字
        if c in "1234567890":
           num = num * 10 + float(c)
        elif c in "+-":  # 检测为加减则要考虑符号问题了
            mul_div()
            stack.append(sign * num)
            num = 0.
            sign = cast[c]
        elif c in "*/":
            mul_div()
            stack.append(num * sign)
            if c in "*":
                stack.append("*")
            else:
                stack.append("/")
            num = 0.
            sign = 1
        elif c in "(":
            if sign == 1:
                stack.append("+")
            else:
                stack.append("-")
            stack.append("(")
            stack.append(0)
            num = 0
            sign = 1
        elif c in ")":
            mul_div()
            stack.append(num * sign)
            temp = stack.pop()
            num = 0
            while str(temp) not in "(+-":
                num += temp
                temp = stack.pop()
            if str(stack.pop()) in "-":
                num = -num
            sign = 1
        else:
            pass
    mul_div()
    stack.append(num * sign)
    return sum(stack)


while True:
    s = input()
    print(calculate(s))
