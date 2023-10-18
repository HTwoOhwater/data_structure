class DoubleStack: # 初始化、空、满、进、出
    def __init__(self):
        self.stack_left = [None for i in range(5)]
        self.stack_right = [None for i in range(5)]
        self.top_left = 0
        self.top_right = 0
        self.empty_left = True
        self.empty_right = True

    def __repr__(self):
        return (f"左栈入栈方向->{self.stack_left + self.stack_right[::-1]}<-右栈入栈方向\n"
                f"左栈长{int(not self.empty_left) + self.top_left}, 右栈长{int(not self.empty_right) + self.top_right}")

    def push(self, position, value):
        if self.is_full():
            raise Exception("Stack Full")

        if not position:
            if self.empty_left:
                self.stack_left[0] = value
                self.empty_left = False
            else:
                self.top_left += 1
                if self.top_left < 5:
                    self.stack_left[self.top_left] = value
                elif self.top_left >= 5:
                    self.stack_right[-self.top_left + 4] = value
        else:
            if self.empty_right:
                self.stack_right[0] = value
                self.empty_right = False
            else:
                self.top_right += 1
                if self.top_right < 5:
                    self.stack_right[self.top_right] = value
                elif self.top_right >= 5:
                    self.stack_left[-self.top_right + 4] = value

    def pop(self, position):
        if not position:
            if self.top_left == 0:
                if self.empty_left is False:
                    temp = self.stack_left[0]
                    self.stack_left[0] = None
                    self.empty_left = True
                else:
                    raise Exception("Stack Empty")
            else:
                if self.top_left < 5:
                    temp = self.stack_left[self.top_left]
                    self.stack_left[self.top_left] = None
                elif self.top_left >= 5:
                    temp = self.stack_right[-self.top_left + 4]
                    self.stack_right[-self.top_left + 4] = None
                self.top_left -= 1
        else:
            if self.top_right == 0:
                if self.empty_right is False:
                    temp = self.stack_right[0]
                    self.stack_right[0] = None
                    self.empty_right = True
                else:
                    raise Exception("Stack Empty")
            else:
                if self.top_right < 5:
                    temp = self.stack_right[self.top_right]
                    self.stack_right[self.top_right] = None
                elif self.top_right >= 5:
                    temp = self.stack_left[-self.top_right + 4]
                    self.stack_left[-self.top_right + 4] = None
                self.top_right -= 1
        return temp

    def is_empty(self):
        return self.empty_left is True and self.empty_right is True

    def is_full(self):
        return int(not self.empty_left) + int(not self.empty_right) + self.top_left + self.top_right >= 10

    def __len__(self):
        return int(not self.empty_left) + self.top_left, int(not self.empty_right) + self.top_right


stack = DoubleStack()
for i in "关注永雏塔菲喵谢谢喵":
    stack.push(0, i)
print(stack)
for i in range(10):
    stack.pop(0)
    print(stack)
print(stack.is_empty())

