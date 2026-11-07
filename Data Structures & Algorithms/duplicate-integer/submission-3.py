class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = {}
        
        for i in range(0,len(nums)):
            count = 0 
            # if cache[cache[i]] >= 1 : 
            #     continue
            # else :
            if nums[i] in cache :
                return True
        
            cache[nums[i]] =  1
    
        return False
        print(cache)