# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制 。
#
#
#
#  实现 LRUCache 类：
#
#
#  LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
#  void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上
# 限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
#
#
#
#
#
#  进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
#
#
#  示例：
#
#
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#
#
#
#
#  提示：
#
#
#  1 <= capacity <= 3000
#  0 <= key <= 3000
#  0 <= value <= 104
#  最多调用 3 * 104 次 get 和 put
#
#  Related Topics 设计
#  👍 1356 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 双链表实现
# 			执行耗时:188 ms,击败了35.74% 的Python3用户
# 			内存消耗:23.6 MB,击败了52.50% 的Python3用户
class DLinkedList:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0  # 用于控制是否超出capacity
        self.head = DLinkedList()  # 头结点
        self.tail = DLinkedList()  # 尾结点
        self.tmp = {}  # hash表缓存已有的key
        self.head.next = self.tail  # 将头结点的next指针指向尾结点
        self.tail.prev = self.head  # 将尾结点的prev指针指向头结点

    def get(self, key: int) -> int:
        if key not in self.tmp:  # 判断key是否在缓存hash表中，不在则直接返回-1
            return -1
        node = self.tmp.get(key)  # 在的话，获取该key对应的结点
        self.moveToHead(node)  # 将该结点移动到头结点，说明这个key最近被用过
        return node.value  # 返回该结点对应值

    def put(self, key: int, value: int) -> None:
        if key not in self.tmp:  # 判断key是否在hash表中，不在则增加
            node = DLinkedList(key, value)  # 创建该结点
            self.addToHead(node)  # 增加到头结点
            self.tmp[key] = node  # 增加到hash表
            self.size += 1  # size+1
            if self.size > self.capacity:  # 判断size是否大于capacity
                removed = self.removeTail()  # 在则删除尾节点，因为尾节点最久未使用
                self.tmp.pop(removed.key)  # 并从hash表中删除该节点
                self.size -= 1  # size-1
        else:
            node = self.tmp.get(key)  # 如果在，则获取，
            node.value = value  # 更新值
            self.moveToHead(node)  # 将该结点移到头结点，表示最近使用
    
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)
    
    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
