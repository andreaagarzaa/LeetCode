class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # Find the maximum number of candies any kid has
        max_candies = max(candies)
        
        # Create the result array by checking for each kid if they will have the greatest number of candies after adding extraCandies
        result = [candies[i] + extraCandies >= max_candies for i in range(len(candies))]
        
        return result
