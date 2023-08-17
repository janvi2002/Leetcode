# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ptr=ListNode(0)   #created a dummy node
        carry=0
        while l1 and l2:  #both are present
            value=l1.val+l2.val+carry
            ptr.next=ListNode(value%10)
            carry=value//10
            ptr=ptr.next
            l1=l1.next
            l2=l2.next
        if l2:   #that means l1 is over so make it equal to l1 and solve in next while loop
            l1=l2
        while l1: #here if l1 is present then it take place if l2 is present then also it runs
            value=l1.val+carry
            ptr.next=ListNode(value%10)
            carry=value//10
            ptr=ptr.next
            l1=l1.next
        
        if carry:   #if carry remainign make a node and add at last
            ptr.next=ListNode(carry)

        return dummy.next
        

