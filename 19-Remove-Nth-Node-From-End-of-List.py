# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        c = 0 # count 
        # Count the total number of nodes 
        while curr:
            c += 1 
            curr = curr.next 
        target = c - n # 5-2 = 3
        temp = head 
        if c ==1 or target ==0:
            return head.next
        for i in range(target-1): # 0-1-2-3
            temp = temp.next
        if n==1:
            temp.next = None
            return head 
        else:
            temp.next = temp.next.next 
        return head 