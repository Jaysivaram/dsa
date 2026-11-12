
def findThreeSum(nums:list[int]) -> list[list[int]]:

    nums = sorted(nums)

    print(nums)

    combination = []

    for i in range(len(nums)):

        if nums[i]>0:
            break

        if i  > 0 and nums[i] == nums[i-1] and nums:
            continue

        left = i +1
        right = len(nums) -1

        while left < right:
            

            sum = nums[i] + nums[left] + nums[right]

            print(f"left and right = {left,right},{nums[i],nums[left],nums[right]},sum={sum},")

            if sum > 0:
                right -=1

            elif sum <0:
                left +=1

            else:
                combination.append([nums[i],nums[left],nums[right]])
                left +=1
                right -=1

                while left < right and nums[left] == nums[left -1]:
                    left +=1
                
                while left < right and nums[right] == nums[right +1]:
                    right -=1


    return combination


print(findThreeSum([-1,0,1,2,-1,-4]))

# print(findThreeSum([0, 0, 0, 0, 0, 1, 1, 2]))

            


