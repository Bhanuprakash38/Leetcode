class Solution:
    def addBinary(self, a: str, b: str) -> str:
        cc=int(a,2)
        dd=int(b,2)
        ee=cc+dd
        ff=bin(ee)[2:]
        return ff
        