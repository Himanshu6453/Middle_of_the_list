class ListNode(object): 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        list_len = 0
        start=nod=head
        while start:
            list_len += 1
            start = start.next
        center = list_len // 2
        count = 0
        while nod:
            if count == center:
                return nod
            else:
                count+=1
                nod = nod.next
