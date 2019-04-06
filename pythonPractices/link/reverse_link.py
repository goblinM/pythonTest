'''
created by goblinM
反转单向和双向链表
时间复杂度o(n),额外空间复杂度为o(1)
如何把一个单链表进行反转？

方法1：将单链表储存为数组，然后按照数组的索引逆序进行反转。

方法2：使用3个指针遍历单链表，逐个链接点进行反转。

方法3：从第2个节点到第N个节点，依次逐节点插入到第1个节点(head节点)之后，最后将第一个节点挪到新表的表尾。

方法4:   递归(相信我们都熟悉的一点是，对于树的大部分问题，基本可以考虑用递归来解决。但是我们不太熟悉的一点是，对于单链表的一些问题，也可以使用递归。可以认为单链表是一颗永远只有左(右)子树的树，因此可以考虑用递归来解决。或者说，因为单链表本身的结构也有自相似的特点，所以可以考虑用递归来解决)

反转单向链表：
    ·

反转双向链表
    ·

'''
# 单向链表
class LinkNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
#双向链表
class DoubleLinkNode:
    def __init__(self,val,next=None,last=None):
        self.val = val
        self.next = next
        self.last = last


class ReverseLinkNode:
    def reverse_single_link(self,head):
        if not head:
            return head
        pre = None
        while head:
            cur = head.next
            head.next = pre
            pre = head
            head = cur
        return pre

    def reverse_double_link(self,head):
        if not head:
            return head
        pre = None
        while head:
            cur = head.next
            head.next = pre
            head.last = cur
            pre = head
            head = cur
        return pre