from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        p: List[int] = [0] * 26
        print(p)
        for i in range(len(tasks)):
            print(ord(tasks[i]) - ord('A'))
            p[ord(tasks[i]) - ord('A')] += 1

        p.sort(reverse=True)
        bank, res = 0, 0

        while len(p) > 0:
            print("\nproces ma ", p[0], "wywolan")
            res += p[0] * n

            bank = res - p.pop(0) + bank
            print("mamy:", bank, "wolnych miejsc")
            while len(p) > 0 and bank - p[0] >= 0:
                print("zajmuje", p[0], "wolnych miejsc")
                bank -= p.pop(0)

        return res

s = Solution()
print(s.leastInterval(["A","A","A","B","B","B"], 2))