from collections import deque
# deque, 양방향 큐 : append(enqueue의 방향), popleft(dequeue의 방향)

# d = deque()
d = deque([3, -9, 10])
d.append(77)
d.appendleft(100)
d.append(92)
for i in range(len(d)):
    print(d.popleft())