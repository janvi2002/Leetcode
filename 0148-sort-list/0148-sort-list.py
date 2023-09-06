# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
#         finding middle
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
#         divide from middle
        mid=slow.next
        slow.next=None
        left=self.sortList(head)
        right=self.sortList(mid)
        
        ans= ListNode(0)
        ptr=ans
        if not left:
            return right
        if not right:
            return left
        
        while left and right:
            if left.val < right.val :
                ptr.next = left
                left=left.next
            else:
                ptr.next=right
                right=right.next
            ptr=ptr.next
        
        if left:
            ptr.next=left
        elif right:
            ptr.next=right
        return ans.next
     
        
#         arr=[]
#         ptr=head
#         while ptr:
#             arr.append(ptr.val)
#             ptr=ptr.next
#         arr.sort()
#         dummy=ListNode(0)
#         ptr=dummy
#         for i in arr:
#             new=ListNode(i)
#             ptr.next=new
#             ptr=ptr.next
        
#         return dummy.next