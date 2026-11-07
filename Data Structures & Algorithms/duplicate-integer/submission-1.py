class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to store unique elements
        seen = set()
        
        # Loop through each element in the list
        for num in nums:
            # If the element is already in the set, we found a duplicate
            if num in seen:
                return True
            # Add the element to the set
            seen.add(num)
        
        # If no duplicates were found, return False
        return False

# Example usage:
solution = Solution()
x = [1, 2, 2, 4]
print(solution.hasDuplicate(x))  # Output: True