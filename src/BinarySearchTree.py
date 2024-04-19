class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    # 노드를 삽입하는 함수
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def preorder_traversal(root):
    # 전위 순회 함수
    result = []
    if root:
        result.append(root.val)            # 루트 먼저 방문
        result += preorder_traversal(root.left)   # 왼쪽 서브트리 순회
        result += preorder_traversal(root.right)  # 오른쪽 서브트리 순회
    return result

def inorder_traversal(root):
    # 중위 순회 함수    
    result = []
    if root:
        result += inorder_traversal(root.left)     # 왼쪽 서브트리 순회
        result.append(root.val)                # 루트 중간에 방문
        result += inorder_traversal(root.right)    # 오른쪽 서브트리 순회
    return result

def postorder_traversal(root):
    # 후위 순회 함수
    result = []
    if root:
        result += postorder_traversal(root.left)   # 왼쪽 서브트리 순회
        result += postorder_traversal(root.right)  # 오른쪽 서브트리 순회
        result.append(root.val)               # 루트 마지막에 방문
    return result

# 예제 사용
root = None
keys = [50, 30, 20, 40, 70, 60, 80]

for key in keys:
    root = insert(root, key)

print("이진 탐색 트리의 전위 순회 결과:", preorder_traversal(root))
print("이진 탐색 트리의 중위 순회 결과:", inorder_traversal(root))
print("이진 탐색 트리의 후위 순회 결과:", postorder_traversal(root))
