class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastOccurence = {}

        curLength, maxLength, beggining = 0, 0, -1
        for i in range(len(s)):
            if s[i] not in lastOccurence.keys():
                lastOccurence[s[i]] = -1

            if lastOccurence[s[i]] < beggining:
                curLength += 1
            else:
                curLength = i - lastOccurence[s[i]]
                beggining = lastOccurence[s[i]] + 1

            lastOccurence[s[i]] = i
            maxLength = max(maxLength, curLength)

        return maxLength


s = Solution()
print("RES:", s.lengthOfLongestSubstring(""))
print("RES:", s.lengthOfLongestSubstring("abcabcbb"))
print("RES:", s.lengthOfLongestSubstring("pwwkew"))
print("RES:", s.lengthOfLongestSubstring("bbb"))
print("RES:", s.lengthOfLongestSubstring("abcdefc"))
print("RES:", s.lengthOfLongestSubstring("1234 $%^"))




