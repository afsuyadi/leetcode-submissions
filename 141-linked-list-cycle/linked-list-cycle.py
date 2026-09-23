class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next: # as long as fast doesnt end (means its cyclic)
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False # return False because head == None, which means it's not cyclic
    