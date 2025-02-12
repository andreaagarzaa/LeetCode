class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Check if concatenation of str1 and str2 in both orders is the same
        if str1 + str2 != str2 + str1:
            return ""

        # Function to compute the greatest common divisor
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # The GCD of the lengths will determine the largest common divisor string
        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]
