class Solution:
    def minIncrementForUnique(self, nums):
        nums.sort()
        li=[]
        incr=0
        for val in nums:
            if val not in li:
                li.append(val)
            else:
                rval=val
                while rval in li:
                    rval+=1
                    incr=incr+1
                li.append(rval)
        return incr