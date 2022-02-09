# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #finding the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reversing order of the second half of our list
        second = slow.next
        previous = None
        slow.next = None
        while second:
            dummy = second.next
            second.next = previous
            previous = second
            second = dummy
        
        #Merge both lists together with proper order
        first, second = head, previous
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
