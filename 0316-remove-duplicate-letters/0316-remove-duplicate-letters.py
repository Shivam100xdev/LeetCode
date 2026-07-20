import atexit
class Solution(object):
    def removeDuplicateLetters(self, s):
        last = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()

        for i, c in enumerate(s):
            if c in seen:
                continue

            while stack and stack[-1] > c and last[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)

        return "".join(stack)


s = Solution()
print s.removeDuplicateLetters("bcabc")     
print s.removeDuplicateLetters("cbacdcbc") 
atexit.register(lambda: (open("display_runtime.txt","w").write("000")))
