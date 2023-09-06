# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        ptr=head
        while ptr:
            arr.append(ptr.val)
            ptr=ptr.next
        arr.sort()
        dummy=ListNode(0)
        ptr=dummy
        for i in arr:
            new=ListNode(i)
            ptr.next=new
            ptr=ptr.next
        
        return dummy.next
            
        