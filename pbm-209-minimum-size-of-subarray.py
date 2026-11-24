# # 209. Minimum Size Subarray Sum
# # Medium
# # Topics
# # premium lock icon
# # Companies
# # Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

# # Example 1:

# # Input: target = 7, nums = [2,3,1,2,4,3]
# # Output: 2
# # Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# # Example 2:

# # Input: target = 4, nums = [1,4,4]
# # Output: 1
# # Example 3:

# # Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# # Output: 0
 

# # Constraints:

# # 1 <= target <= 109
# # 1 <= nums.length <= 105
# # 1 <= nums[i] <= 104


# def divide(nums):

#     if(len(nums) ==1): return nums
#     mid = len(nums) // 2

#     left = divide(nums[:mid])

#     right = divide(nums[mid:])

#     return merge(left,right)


# def merge(left,right):

#     i = 0

#     j = 0

#     result = []

#     while i<len(left) and j<len(right):

#         if left[i] < right[j]:

#             result.append(left[i])
#             i += 1

#         else:
#             result.append(right[j])
#             j += 1


    
#     result.extend(left[i:])
#     result.extend(right[j:])


#     return result

# def minimumSubArraySize(nums,k):

#     nums = divide(nums)

#     windowSize = nums[0]

#     left = 0
#     right =1

#     if nums[0] == k: return


#     for i in range(right,len(nums) -1):

#         windowSize += nums[i]

#         if windowSize == k:

#             windowSize -=[nums[left]]

#             left -=1


#         elif windowSize < k:

#             right+=1

#         else: break





#     print(nums,left,right)


        



   




# minimumSubArraySize([2,3,1,2,4,3],7)

