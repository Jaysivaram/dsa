# 215. Kth Largest Element in an Array
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
 

# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

def devide(nums):

    if len(nums) ==1:
        return nums

    mid = len(nums)// 2

    left = devide(nums[:mid])
    right = devide(nums[mid:])

    return merge(left,right)


def merge(left,right):

    i = 0
    j = 0

    result = []

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i +=1

        else:
            result.append(right[j])
            j +=1

    
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def findKthLargestNumber(nums,k):
    

    nums = devide(nums)
    print(nums)

    return nums[len(nums)-k]


print(findKthLargestNumber([3,2,1,5,6,4],6))





