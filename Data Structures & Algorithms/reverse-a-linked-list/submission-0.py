# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head          # node we're standing on
        prev = None         # node behind us (old head becomes new tail -> None)

        while cur:
            temp = cur.next     # save the map before we tear it up
            cur.next = prev     # THE FLIP: point backwards
            prev = cur          # shuffle prev forward
            cur = temp          # shuffle cur forward using the saved pointer

        return prev         # cur is None; prev is the last real node = new head

        
        # Time: O(n)
        # Space: O(1)