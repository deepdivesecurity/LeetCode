class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[],[]]

        for i in nums1: 
            if i not in nums2 and i not in answer[0]: 
                answer[0].append(i)

        for y in nums2: 
            if y not in nums1 and y not in answer[1]: 
                answer[1].append(y)

        return answer
