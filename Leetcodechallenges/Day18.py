class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        
        # Calculate the length of the list
        while curr:
            length += 1
            curr = curr.next
        
        # Use a dummy node to simplify edge cases
        dummy = ListNode(0, head)
        curr = dummy
        
        # Find the node just before the one we want to remove
        for _ in range(length - n):
            curr = curr.next
        
        # Remove the nth node from the end
        if curr.next:
            curr.next = curr.next.next
        
        return dummy.next
        