class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]  # M�ximo global
        current_sum = nums[0]  # M�ximo local

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)  # Reiniciar o continuar la suma
            max_sum = max(max_sum, current_sum)  # Actualizar el m�ximo global

        return max_sum
