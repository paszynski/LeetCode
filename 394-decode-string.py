from typing import List

class Solution:
    def decodeString(self, s: str) -> str:
        stack: List[str] = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                encoded_string = stack.pop()
                while encoded_string[0] != "[":
                    encoded_string = stack.pop() + encoded_string
                encoded_string = encoded_string[1:]

                k, p = 0, 1
                while len(stack) > 0 and len(stack[-1]) == 1 and ord(stack[-1]) >= 48 and ord(stack[-1]) <= 57:
                    k += (ord(stack.pop()) - 48) * p
                    p *= 10

                stack.append(encoded_string * k)

        return "".join(stack)


s = Solution()
print(s.decodeString("3[a]2[bc]"))
print(s.decodeString("3[a2[c]]"))
print(s.decodeString("2[abc]3[cd]ef"))

