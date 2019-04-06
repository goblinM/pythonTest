'''
created by goblinM
反转部分单向链表
给定一个单向链表的头结点head,以及两个整数from和to,
在单向链表上把第from个节点到第to个节点这一部分进行反转
1->2->3->4->5->null,from=2,to=4
结果为1->4->3->2->5->null
时间复杂度为o(N),额外空间复杂度为o(1)
如果不满足1<=from<=to<=N,则不用调整。
思路：
    ·判断1<=from<=to<=N
    ·找到第from-1个节点fpre,和第to+1个节点tpos.fpre反转部分的前一个节点，tpos是反转部分的
    后一个节点。把反转的部分先反转，然后正确的连接fpre和tpos
    ·如果fpre为null,说明反转部分包含头结点，则返回新的头结点，也就是没反转之前反转部分的最后
    一个节点，也是反转之后反转部分的第一个结点。
'''
class LinkNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class ReverseOtherLink:
    def reverse_other_link_node(self,head,f,t):
        head_len = 0
        cur = head
        fpre = None
        tpos = None
        while cur:
            head_len += 1
            fpre = cur if head_len==f-1 else fpre
            tpos = cur if head_len==t+1 else tpos
            cur = cur.next
        if f>t or f<1 or t>head_len:
            return head
        cur = head if not fpre else fpre.next
        node2 = cur.next
        cur.next = tpos
        while node2:
            next = node2.next
            node2.next = cur
            cur = node2
            node2 = next
        if fpre:
            fpre.next = cur
            return head
        return cur

