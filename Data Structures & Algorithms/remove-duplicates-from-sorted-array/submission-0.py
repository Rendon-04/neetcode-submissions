class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_numbers = 1  
        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                nums[new_numbers] = nums[index]
                new_numbers += 1
        return new_numbers
            


nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
k = sol.removeDuplicates(nums)
print("k =", k)                 
print("uniques =", nums[:k])    
print("nums after =", nums)  

