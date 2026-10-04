class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # dummy nodes
        self.left = Node(0, 0)   # LRU side
        self.right = Node(0, 0)  # MRU side

        self.left.next = self.right
        self.right.prev = self.left


    # 从链表删除 node
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev


    # 插到最右边，表示 most recently used
    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # 刚被访问 → 移到 MRU
        self.remove(node)
        self.insert(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        # 如果已经存在，先删除旧节点
        if key in self.cache:
            self.remove(self.cache[key])

        # 创建新节点并放到 MRU
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # 超过容量 → 删除 LRU
        if len(self.cache) > self.capacity:
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]