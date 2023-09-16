# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # First find the middle element by two pointer
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        # divide it into two parts 
        middle = slow
        right = middle.next 
        middle.next = None
        # Reverse the second part 
        prev, cur = None, right
        while cur:
            nxt = cur.next 
            cur.next = prev 
            prev = cur
            cur = nxt 
        # Rember the first element and start adding
        left = head 
        right = prev 
        while left and right:
            temp1 = left.next
            temp2 = right.next
            right.next = None 
            left.next = right
            right.next = temp1
            left = temp1
            right = temp2
         


        