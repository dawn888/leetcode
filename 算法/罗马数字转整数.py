class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a=0
        temp=0
        n1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n2={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        list=[]
        result_s=s
        for i in n2.keys():
            if i in (s):
                a+=n2[i]
                list.append(i)
                result_s=result_s.replace(i,"")
        for i in result_s:
            a+=n1[i]
        return a


        # for key,value in enumerate(s):
        #    print(value,n1[value],temp)
        #    if(temp>n1[value]):
        #        a = a + n1[value]
        #    else:
        #        a = n1[value]-temp
        #        temp=n1[value]
        # print(a)


solution=Solution()
s="IV"
solution.romanToInt(s)

#M = 1000, CM = 900, XC = 90, IV = 4
#If I comes before V or X, subtract 1 eg:
#If X comes before L or C, subtract 10 eg:
#If C comes before D or M, subtract 100 eg: