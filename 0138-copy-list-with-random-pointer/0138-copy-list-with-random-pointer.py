"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
#      with extra space map
        hashmap={}
        ptr=head
        while ptr:
            hashmap[ptr] = Node(ptr.val)
            ptr=ptr.next
        
        ptr=head
        while ptr:
            n=hashmap[ptr]
            n.next=hashmap[ptr.next] if ptr.next else None
            n.random=hashmap[ptr.random] if ptr.random else None
            ptr=ptr.next
            
        return hashmap[head]
    