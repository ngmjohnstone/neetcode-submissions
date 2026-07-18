# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        current_list = head

        while current_list:
            temp = current_list.next
            current_list.next = new_list
            new_list = current_list
            current_list = temp
        return new_list
        