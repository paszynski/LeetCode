class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split(" ")
        res = ""
        for i in range(len(ss)-1, -1, -1):
            if len(ss[i]) > 0:
                res += ss[i] + " "
        return res[:-1]

s = Solution()
print(s.reverseWords("the sky is blue"))
print(s.reverseWords("  hello world!  "))
print(s.reverseWords("a good   example"))