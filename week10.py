class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


def pre_order(node):
    if node is None:
        return
    print(node.data, end="->")
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end="->")
    in_order(node.right)


def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end='-')


def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None: # 첫 번째 노드일 때 처리
        return new_node

    current = root

    while True:
        if value < current.data:
            if current.left is None:
                current.left = new_node
                break
            current = current.left  # move
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right  # move
    return root


def search(number):
    search_value = number
    current = root
    while True:
        if search_value == current.data:
            return True
        elif search_value < current.data:
            if current.left is None:
                return False
            current = current.left
        else:
            if current.right is None:
                return False
            current = current.right


def delete(node, value):
    if node is None:
        return None

    # 삭제할 노드 찾아 이동
    if value < node.data:
        node.left = delete(node.left, value)
    elif value > node.data:
        node.right = delete(node.right, value)
    else:
        # 삭제할 노드 발견
        # 자식이 없는 leaf 노드거나 자식이 하나만 있는 경우
        if node.left is None:
            return node.right # 재귀 함수가 return 값을 받음
        elif node.right is None:
            return node.left
        # 자식이 2개인 경우
        min_larger_node = node.right
        while min_larger_node.left: # 오른쪽 트리에서 가장 작은 값 찾기
            min_larger_node = min_larger_node.left # move
        node.data = min_larger_node.data
        node.right = delete(node.right, min_larger_node.data)
    return node

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 14]
    root = None

    for number in numbers:
        root = insert(root, number)

    print("BST 구성 완료")

    pre_order(root)
    print()

    number = int(input("찾고자 하는 값: "))
    if search(number):
        print(f"{number}을(를) 찾았습니다")
    else:
        print(f"{number}이(가) 존재하지 않습니다")

    del_number = int(input("제거하고자 하는 값: "))
    root = delete(root, del_number)
    pre_order(root)
