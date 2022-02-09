# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def LaczenieList(self, lista1: ListNode, lista2: ListNode) -> ListNode:
        if not lista1: return lista2
        if not lista2: return lista1
            
        current=tmp=ListNode(0)
        while lista1 and lista2:
            if lista1.val < lista2.val:
                current.next = lista1
                lista1 = lista1.next
            else:
                current.next=lista2
                lista2=lista2.next
            current = current.next
        if lista1: current.next = lista1
        if lista2: current.next = lista2
                    
        return tmp.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        elif len(lists)==1:
            return lists[0]
        else:
            output = lists[0]
            
        for i in range(1, len(lists)):
            output = self.LaczenieList(output, lists[i])
        return output
