class Solution:
    def lengthOfLastWord(self, s):
        y=s.strip()
        l=0
        for i in range (len(y)):
            if y[i]==" ":
                l=0
            else:
                l+=1
        return l