class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head: # LinkedList에 Node가 하나도 없으면
            self.head = Node(data) # 새 노드를 head에 연결
            return
        current = self.head
        while current.link:
            current = current.link # 다음 노드로 이동
        current.link = Node(data)

    def __str__(self):
        node = self.head
        out_texts = ""
        while node is not None: # node 없으면 false
            # print(node.data)
            out_texts = out_texts + str(node.data) + " -> "
            node = node.link
        return out_texts + "end"


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)

print(ll)