from data_structure import *

"""
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 3:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

next(myiter)
next(myiter)
next(myiter)
"""
stack = Stack()
stack.show_stack()
for i in range(5):
    stack.push(Node(i))
stack.show_stack()
stack.pop()
stack.show_stack()