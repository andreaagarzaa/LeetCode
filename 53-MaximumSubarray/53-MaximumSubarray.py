class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]  # Máximo global
        current_sum = nums[0]  # Máximo local

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)  # Reiniciar o continuar la suma
            max_sum = max(max_sum, current_sum)  # Actualizar el máximo global

        return max_sum
