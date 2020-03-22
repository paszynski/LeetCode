class Solution:
    def primePalindrome(self, N: int) -> int:
        primes = [2,3,5,7,11,101,131,151,181,191,313,353,373,383, 727,757,787,797,919,929,10301,10501,10601,11311, 11411,12421,12721,12821,13331,13831,13931,14341, 14741,15451,15551,16061,16361,16561,16661,17471, 17971,18181]
        i = 0
        while primes[i] < N:
            i += 1
        return primes[i]


s = Solution()
print(s.primePalindrome(6))
print(s.primePalindrome(8))
print(s.primePalindrome(13))
print(s.primePalindrome(1300))
print(s.primePalindrome(100000000))
print(s.primePalindrome(199999999))