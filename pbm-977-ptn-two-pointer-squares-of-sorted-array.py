# 977. Squares of a Sorted Array
# Easy
# Topics
# premium lock icon
# Companies
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
 

# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?


#using buble sort approach
def squaresOfArr(nums):


        for i in range(len(nums)):
            convertion = abs(nums[i])
            nums[i] = convertion * convertion


        for i in range(len(nums)-1):

            left = 0
            right = 1
            swap = False

            for j in range(len(nums)-1):

                if nums[left] > nums[right]:
                    
                    nums[left],nums[right] = nums[right],nums[left]

                    swap = True

                left +=1
                right +=1



            if swap != True:
                break


        print(nums)


squaresOfArr([-4,-1,0,3,10])


#using two pointer approach
def squaresOfArr1(nums):

        temp = [0] * len(nums)
        
        left = 0
        right = len(nums) -1
        k = len(nums) -1

        while right>=left:

            
            if abs(nums[left]) > abs(nums[right]):
               temp[k] = nums[left] ** 2

               left +=1
            else:
                temp[k] = nums[right] ** 2
                right -= 1

            print(temp)
            
            k-=1
            

    

            
squaresOfArr([-5, -4, -3, 1, 2])   



        


