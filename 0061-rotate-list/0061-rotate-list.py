# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
#         count the length
        c=1
        ptr=head
        while ptr.next:
            c+=1
            ptr=ptr.next
#         making circular ll 
        ptr.next=head
        k=k%c
#         checking the last node
        last=c-k
        while last:
            ptr=ptr.next
            last-=1
#         point the actual head and make last node pointing to Null
        head=ptr.next
        ptr.next=None
        
        return head