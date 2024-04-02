class Solution:
    def reverseWords(self, s: str) -> str:
        answerList = s.split()
        answerList.reverse()

        answer = " ".join(str(i) for i in answerList)

        return answer
