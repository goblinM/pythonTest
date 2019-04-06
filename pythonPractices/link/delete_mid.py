'''
created by goblinM
删除链表的中间节点和a/b处的节点
链表为空或长度为1直接返回
长度为2：删除头结点
长度为3：删除第二个节点
。。。
中间节点：
也就是链表长度每增加2(3,5,7...)删除的节点就我往后移一个节点
给定链表的头结点head,整数a和b,实现删除位于a/b处节点的函数:
先计算r = (a*n)/b的值，然后r向上取整之后的整数值代表该删除的节点是第几个节点
'''
class LinkNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class DeleteMidAB:
    def delete_middle_node(self,head):
        if not head or head.next == None:
            return head
        if head.next.next == None:
            return head.next
        pre = head.next
        cur = head.next.next
        while cur.next != None and cur.next.next != None:
            pre = pre.next
            cur = cur.next.next
        pre.next = pre.next.next
        return head

    def delete_ab_node(self,head,a,b):
        if a < 1 or a > b:
            return head
        head_len = 0
        cur = head
        while cur:#计算长度
            head_len += 1
            cur = cur.next
        n = int((a*head_len)/b)
        if n == 1:
            head = head.next
        if n > 1:
            cur = head
            while n-1 != 1:
                cur = cur.next
            cur.next = cur.next.next
        return head