class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False


solution = Solution()

x= [1,2,3,4]

print(solution.hasDuplicate(x))