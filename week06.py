class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        self.size = self.size + 1
        node = Node(data)
        if self.rear == None: # 큐에 아무것도 없으면
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node


q = Queue()
q.enqueue("Data Structure")
q.enqueue("Database")
print(q.size, q.front.data, q.rear.data)