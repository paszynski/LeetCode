# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printList(self):
        res = str(self.val)
        pom = self
        while pom.next != None:
            pom = pom.next
            res += " -> " + str(pom.val)
        print(res)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum1 = l1.val
        multiplier1 = 1
        sum2 = l2.val
        multiplier2 = 1

        while l1.next != None:
            multiplier1 *= 10
            l1 = l1.next
            sum1 += l1.val * multiplier1


        while l2.next != None:
            multiplier2 *= 10
            l2 = l2.next
            sum2 += l2.val * multiplier2


        #print("sum1:", sum1, " sum2:", sum2)
        return self.convertNumberToList(sum1+sum2)

    def convertNumberToList(self, number: int) -> ListNode:
        res = ListNode(number % 10)
        number //= 10
        tail = res

        while number > 0:
            ln = ListNode(number % 10)
            number //= 10
            tail.next = ln
            tail = ln

        return res

    def printList(self):
        res = str(self.val)
        pom = self
        while pom.next != None:
            pom = pom.next
            res += " -> " + str(pom.val)
        print(res)


s = Solution()
l1 = s.convertNumberToList(342)
l2 = s.convertNumberToList(465)

#l1.printList()
#l2.printList()

l3 = s.addTwoNumbers(l1, l2)

