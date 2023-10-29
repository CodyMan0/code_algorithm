# Valid Parentheses
def isValid(s):
    stack = []
    pairs = {"(": ")", "{": "}", "[": "]"}
    for bracket in s:
        if bracket in pairs:
            stack.append(bracket)

        elif len(stack) == 0 or bracket != pairs[stack.pop()]:
            return False

    return len(stack) == 0

    ### isValid("()")

    ## IDEA : LIFO principle. therefore a stack is a good choice here

    # Merge Two Sorted Lists


def mergeTwoLists(list1, list2):
    head = ListNode()
    current = head
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    current.next = list1 or list2
    return head.next


mergeTwoLists([-1, -2], [1, 3, 4])

## 두 배열 깊게 복사한 후 sort 돌리면 안되나?

## 연결 리스트와 관련된 질문이었다.

## 둘다 오름차순으로 정렬되어있음.슬라이딩? 알고리즘 사용하면 안되나?

# Remove Duplicates from Sorted Array


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        replace = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[replace] = nums[i]
                replace += 1
        return replace
