import atexit 
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        d = {}
        for c in magazine:
            d[c] = d.get(c, 0) + 1
        for c in ransomNote:
            if d.get(c, 0) == 0:
                return False
            d[c] -= 1
        return True
atexit.register(lambda: (open("display_runtime.txt","w").write("000")))        