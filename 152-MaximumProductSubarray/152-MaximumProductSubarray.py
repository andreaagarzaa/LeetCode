class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                max_product, min_product = min_product, max_product  # Intercambio cuando hay un n�mero negativo

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            result = max(result, max_product)

        return result

