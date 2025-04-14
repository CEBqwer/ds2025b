class Minstack():
    def __init__(self):
        self.main = [] # push, pop
        self.min = [] # 가장 작은 요소를 항상 추적

    def push(self, n):
        if len(self.main) == 0: # main 비어 있으면 n은 무조건 가장 작은 값
            self.min.append(n)
        elif n <= self.min[-1]: # min의 마지막 요소는 항상 스택에서 가장 작은 값
            self.min.append(n)
        else: # min의 마지막 요소보다 크면
            self.min.append(self.min[-1])
        self.main.append(n)

    def pop(self):
        self.min.pop()
        return self.main.pop()

    def get_min(self):
        return self.min[-1]


min_stack = Minstack()
min_stack.push(10)
print(min_stack.main)
print(min_stack.min)

min_stack.push(30)
print(min_stack.main)
print(min_stack.min)
print(min_stack.get_min())