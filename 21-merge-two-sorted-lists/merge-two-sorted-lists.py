from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
                
            else: #  list1.val >= list2.val
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2
        return dummy.next

def built_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def print_listnode(ListNode):
    result = []
    while ListNode:
        result.append(ListNode.val)
        ListNode = ListNode.next
        
    return result
        