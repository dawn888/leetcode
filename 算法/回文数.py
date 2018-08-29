class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a_list=[]
        for i in str(x):
            a_list.append(i)
        b_list=str(a_list)
        a_list.reverse()
        return (str(a_list)==str(b_list))


solution=Solution()
print(solution.isPalindrome(1212))