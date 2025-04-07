class Stack:
    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop() # 리턴 후 삭제


    def size(self):
        return len(self.items) # self : 실행 시점의 객체


    def is_empty(self):
        return len(self.items) == 0


    def peek(self):
        return self.items[-1] # 리턴만


s1 = Stack()
s2 = Stack()

print(s1.is_empty())
s1.push("자료구조")
print(s1.is_empty())
print(s2.is_empty())
s1.push("데이터베이스")
print(s1.size())
print(s1.peek())
print(s1.pop())
print(s1.size())