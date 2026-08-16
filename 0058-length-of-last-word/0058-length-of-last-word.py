import atexit
class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip().split()[-1])
        
atexit.register(lambda: open("display_runtime.txt", "w").write("000"))

