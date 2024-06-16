class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i= 0
        while nums :
            p1, p2 = nums.pop(), nums.pop()
            i+= p2
        return i