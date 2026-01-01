class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] > 9 and i == 0:
                digits[i] = digits[i] % 10
                digits.insert(0,1)
            elif digits[i] > 9:
                digits[i] = digits[i]%10
                digits[i - 1] += 1
            
        return digits