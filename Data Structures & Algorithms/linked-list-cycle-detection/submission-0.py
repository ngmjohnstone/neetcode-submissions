# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        chains = []
        while head:
            chain = head.next
            if chain in chains:
                return True
            chains.append(chain)
            head = chain
        return False
        