from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # transform graph
        subordinates = dict()
        for employee, manager in enumerate(manager):
            if manager != -1:
                subordinates.setdefault(manager, []).append(employee)
        #print(subordinates)

        def getEmployeeResult(employee, overhead):
            # result is employee overhead time + max of all subordinates results
            maxSubordinate = 0
            for subordinate in subordinates.get(employee, []):
                maxSubordinate = max(
                    maxSubordinate, 
                    getEmployeeResult(subordinate, informTime[employee])
                )            
            #print('employee: {}, overhead: {}, maxSubordinate: {}'.format(employee, overhead, maxSubordinate))
            return overhead + maxSubordinate

        return getEmployeeResult(headID, 0)   

def test(n:int, headID:int , manager:[], informTime:[]):
    solution = Solution()
    print("n={}, headID={}, manager={}, informTime={}".format(n,headID, manager, informTime))
    print(solution.numOfMinutes(n,headID, manager, informTime))


test(1, 0, [-1], [0])
test(7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1])
test(7, 0, [-1,0,0,1,3,4,2], [1,1,2000,1,1,1,1])
