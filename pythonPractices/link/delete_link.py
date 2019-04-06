'''
created by goblinM
在单链表和双链表中删除倒数第K个节点
思路：链表为空或k小于1.返回即可
让链表从头开始走到尾，没移动一步，就让k值减1
如果k值大于0，表示没有此节点，直接把链表返回
k等于0，表示链表的倒数第k个节点就是此节点
此时直接返回head.next.
k小于0，重新从头结点开始走，每移动一步,就让k的值加1.
k等于0时，停止移动，移动到的节点就是要删除节点的前一个节点。
删除第k个节点，倒数第k个节点的前一个节点就是第N-K个节点。在第一次遍历后，k
k的值变为k-N，第二次遍历是，k的值不断加1，加到0就停止遍历，第二次遍历当然会停到第N-K
个节点的位置。
'''
class LinkNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkDoubleNode:
    def __init__(self,val,next=None,last=None):
        self.val = val
        self.next = next
        self.last = last

class DeleteLink:
    '''单链表'''
    def delete_link_node(self,s,n):
        if not s or n < 1:
            return s
        p = s
        while p:
            n -= 1
            p = p.next
        if n == 0:#等于0直接返回
            return s.next
        elif n < 0:#小于0
            p = s
            while n + 1 != 0:
                p = p.next
                n += 1
            p.next = p.next.next
        return s

    def delete_link_node2(self,s,n):
        if not s or n < 1:
            return s
        # 快慢指针,当fast指针和slow再次相遇
        fast = slow = s
        while n > 0:
            n -= 1
            if fast == None:
                return s
            else:
                fast = fast.next
        if fast == None:
            return s.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return s

    '''双链表和单链表指针处理方式一致，但是注意last指针的重连就好'''
    def delete_double_link_node(self,s,n):
        if not s or n < 1:
            return s
        cur = s
        while cur:
            n -= 1
            cur = cur.next
        if n == 0:
            s = s.next
            s.last = None
        elif n < 0:
            cur = s
            while n+1 != 0:
                cur = cur.next
                n += 1
            cur.next = cur.next.next
            if cur.next:
                cur.next.last = cur
        return s

    def delete_double_link_node2(self,s,n):
        if not s or n < 1:
            return s
        fast = slow = s
        while n > 0:
            n -= 1
            if fast != None:
                fast = fast.next
            else:
                return s
        if fast == None:
            s = s.next
            s.last = None
        else:
            while fast.next != None:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next
            if slow.next:
                slow.next.last = slow
        return s

if __name__ == "__main__":
    node = LinkNode(1,LinkNode(2,LinkNode(5,LinkNode(6,LinkNode(8)))))
    n = 3
    obj = DeleteLink()
    r = obj.delete_link_node(node,n)
    print(r)