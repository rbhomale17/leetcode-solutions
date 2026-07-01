# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # Create two runner
        first_runner = dummy
        second_runner = dummy
        # provide head start to first_runner by N+1
        for i in range(n+1):
            first_runner = first_runner.next
        # run until first_runner is None or empty so second_runner will point on N-1 element
        while first_runner:
            first_runner = first_runner.next
            second_runner = second_runner.next
        # second_runner is pointing on N-1 element so assign it next to next.next skiping Nth value
        second_runner.next = second_runner.next.next
        
        return dummy.next

