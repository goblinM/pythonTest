'''
链表
'''

class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    # 1.反转链表
    def reverseList(self, head: 'ListNode') -> 'ListNode':
         if not head:
             return None
         p = None
         q = None
         r = head
         while r.next:
             q = p
             p = r
             r = r.next
             p.next = q
         r.next = p
         return r

