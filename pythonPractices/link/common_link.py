'''
created by goblinM
打印两个有序链表的公共部分
思路：
1->2->3->5->6->7
2->4->5->6->8
公有部分：2,5,6
  ·head1.val < head2.val,head1下移
  ·head1.val > head2.val,head2下移
  ·head1.val == head2.val 打印这个值，存入，head1,head2都下移
  ·head1 或者head2中移动到none，则停止
'''

class LinkNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class CommonLink:
    def get_common(self,link1,link2):
        head1 = link1
        head2 = link2
        res = []
        while head1 and head2:
            if head1.val< head2.val:
                head1 = head1.next
            elif head1.val > head2.val:
                head2 = head2.next
            else:
                res.append(head1.val)
                head1 = head1.next
                head2 = head2.next

        return res

if __name__ == "__main__":
    obj = CommonLink()
    link1 = LinkNode(1,LinkNode(2,LinkNode(3,LinkNode(5,LinkNode(6,LinkNode(7))))))
    link2 = LinkNode(1, LinkNode(2, LinkNode(4, LinkNode(5, LinkNode(6, LinkNode(8))))))
    print(obj.get_common(link1,link2))