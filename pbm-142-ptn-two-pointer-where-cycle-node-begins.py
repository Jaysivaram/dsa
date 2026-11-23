
# # 142. Linked List Cycle II
# # Medium
# # Topics
# # premium lock icon
# # Companies
# # Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# # There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# # Do not modify the linked list.

 

# # Example 1:


# # Input: head = [3,2,0,-4], pos = 1
# # Output: tail connects to node index 1
# # Explanation: There is a cycle in the linked list, where tail connects to the second node.
# # Example 2:


# # Input: head = [1,2], pos = 0
# # Output: tail connects to node index 0
# # Explanation: There is a cycle in the linked list, where tail connects to the first node.
# # Example 3:


# # Input: head = [1], pos = -1
# # Output: no cycle
# # Explanation: There is no cycle in the linked list.
 

# # Constraints:

# # The number of the nodes in the list is in the range [0, 104].
# # -105 <= Node.val <= 105
# # pos is -1 or a valid index in the linked-list.


# class Node:
#     def __init__(self,newData):


#         self.data = newData
#         self.next = None


# head = Node(10)

# head.next = Node(20)

# head.next.next = Node(30)

# head.next.next.next = Node(40)

# head.next.next.next.next = head.next

# def findCycleStart(node):

#     slow = node
#     fast = node

#     while fast is not None and fast.next is not None:
#         slow = slow.next
#         fast = fast.next.next



#         if fast is slow:
#             break
#     else:
#         return None

#     slow = node
#     while slow is not fast:
#         slow = slow.next
#         fast = fast.next

#     return slow.data



# print(findCycleStart(head))

# 347. Top K Frequent Elements
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]

 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.


import heapq


def findTopKFrequentElements(nums,k):

    hashList = {}

    frequentList = []

    result = []

    for i in nums:

      hashList[i] =  hashList.get(i,0)+1


    for num,count in hashList.items():

        heapq.heappush(frequentList,(-count,num))

    
    for _ in range(k):

        count,num = heapq.heappop(frequentList)
        result.append(num)


    return result





findTopKFrequentElements([1,2,1,2,1,2,3,1,3,2],3)


    