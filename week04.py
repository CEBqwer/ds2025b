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

    def remove(self, target):
        if self.head.data == target: # 지우려는 게 head 노드일 경우
            self.head = self.head.link
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.link = current.link
            previous = current
            current = current.link

    def search(self, target):
        current = self.head
        # while current.link: # << 마지막 왔을 때 링크가 None이기 때문에, 마지막 노드 때는 안 돌음... -> 마지막 노드를 못 찾는다
        while current:
            if current.data == target:
                return f"{target}을(를) 찾았습니다."
            else:
                current = current.link # 다음 노드로 이동
        return f"{target}은(는) 링크드 리스트 안에 존재하지 않습니다."

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
print(ll.search(100))
print(ll.search(-9)) # << -9는 링크드 리스트 안에 존재하지 않습니다.

ll.remove(0) # 없는 노드일 경우
ll.remove(8) # 첫 번째 노드일 경우
ll.remove(-9)
print(ll)