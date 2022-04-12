# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        number = 0
        
        #finding number of elements and middle point of linked list
        while current:
            number+=1
            current = current.next
        middle = number//2
        i=0
        
        #reversing linked list
        def odwrotnosc(head):
            tmp = None
            while head:
                nx=head.next
                head.next = tmp
                tmp = head
                head = nx
            return tmp
        
        #Reverse the second part of linked list 
        first = second = head
        while i<middle:
            second = second.next
            i+=1
        second = odwrotnosc(second)
        
        
        #checking if values form first part are equal to the values from the second part of the linked list
        while first and second:
            if first.val != second.val: return False
            first = first.next
            second = second.next
        return True
