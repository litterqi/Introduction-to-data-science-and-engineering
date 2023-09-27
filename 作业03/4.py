# 链表节点类
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
# 链表类
class LinkedList:
    def __init__(self):
        self.head = None
    # 在链表末尾添加节点
    def append(self, data):
        node = ListNode(data)
        if not self.head:
            self.head = node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = node
    # 在指定位置插入节点
    def insert(self, index, data):
        if index < 0:
            return False
        elif index == 0:
            node = ListNode(data)
            node.next = self.head
            self.head = node
            return True
        else:
            curr_node = self.head
            for i in range(index - 1):
                curr_node = curr_node.next
                if not curr_node:
                    return False
            node = ListNode(data)
            node.next = curr_node.next
            curr_node.next = node
            return True
    # 删除指定位置的节点
    def delete(self, index):
        if not self.head or index < 0:
            return False
        elif index == 0:
            self.head = self.head.next
            return True
        else:
            curr_node = self.head
            for i in range(index - 1):
                curr_node = curr_node.next
                if not curr_node.next:
                    return False
            curr_node.next = curr_node.next.next
            return True
    # 获取指定位置的节点值
    def get(self, index):
        if not self.head or index < 0:
            return None
        else:
            curr_node = self.head
            for i in range(index):
                curr_node = curr_node.next
                if not curr_node:
                    return None
            return curr_node.data
    # 将链表打印出来
    def print(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()
# 示例测试
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.print()  # 输出：1 2 3
llist.insert(1, 4)
llist.print()  # 输出：1 4 2 3
llist.delete(2)
llist.print()  # 输出：1 4 3
print(llist.get(1))  # 输出：4