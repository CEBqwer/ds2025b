class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class Stack:
    def __init__(self):
        self.top = None


    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.link = self.top
            self.top = node


    def pop(self):
        if self.top is None:
            return "Stack is empty. Nothing to delete."
        popped_node = self.top
        self.top = self.top.link
        return popped_node.data


s1 = Stack()
print(s1.pop())
s1.push("Data Structure")
s1.push("Database")
# print(s1.pop())
# print(s1.pop())
for i in range(3):
    print(s1.pop())