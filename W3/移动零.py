class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left+=1

        for i in range(left,len(nums)):
            nums[i] = 0
        return nums
solution = Solution()
print(solution.moveZeroes([0,1,0,3,12]))
