class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        list=[]
        nums=0
        for i in digits:
            nums=nums*10+i
        nums=nums+1
        for val in str(nums):
            list.append(int(val))
        return list


if __name__ == '__main__':
    digits = [1,2,3]
    solution = Solution()
    print(solution.plusOne(digits))
