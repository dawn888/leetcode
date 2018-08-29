class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min_mt=-2**31
        max_mt=2**31-1
        a_list = []
        if x>=min_mt & x<=max_mt:
            for i in str(abs(x)):
                a_list.append(i)
            a_list.reverse()
            result=int(''.join(a_list))
            if x >= 0 and result<=max_mt:
                return result
            elif(x < 0 and result<=max_mt-1):
                return 0-result
            else:
                return 0


        else:
            return 0

    def reverse1(self,x):
        rev=0
        while (x!=0):
            pop=x%10
            x=int(x/10)
            print(pop,x)
            rev=rev*10+pop
        return int(rev)



solution=Solution()
print(solution.reverse1(153423))