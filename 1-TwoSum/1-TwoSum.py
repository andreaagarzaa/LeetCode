class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}  # Diccionario para almacenar números e índices

        for index, num in enumerate(nums):
            # Calcular lo necesario para llegar al target
            complement = target - num

            # Verificar si el complemento existe en el diccionario
            if complement in dic:
                return [dic[complement], index]

            # Almacenar el número con su índice
            dic[num] = index

        # Retorna una lista vacía si no se encuentra una solución (aunque el problema garantiza que hay una)
        return []

