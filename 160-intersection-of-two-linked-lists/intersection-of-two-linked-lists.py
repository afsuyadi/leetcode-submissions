# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB
        while a != b: # we loop through all distance
            # if they have INTERSECTION,
            # length of A = a + c
            # length of B = b + c
            # point a travels = (a + c) + b
            # point b travels = (b + c) + a
            a = a.next if a else headB # if a is none, switch to headB
            b = b.next if b else headA # is b is none, switch to headA
            
        return a
    