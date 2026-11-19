# 876. Middle of the Linked List
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

 

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
# Example 2:


# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100
 

class Node:
    def __init__(self,newData):


        self.data = newData
        self.next = None


head = Node(20)

head.next = Node(30)

head.next.next = Node(40)

head.next.next.next = Node(50)

def findMiddleOfLinkedList(nodes):


    slow = nodes
    fast = nodes

    out = []

    while fast is not None and fast.next is not None:

        slow = slow.next
        fast = fast.next.next


    return slow


print(findMiddleOfLinkedList(head))

 