# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        previous = None

        while head is not None:
            next_node = head.next
            head.next = previous
            previous = head
            head = next_node

        head = previous

        return head

        