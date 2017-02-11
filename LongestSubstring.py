class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        charList = list(s)
        stack = []
        i = j = maxL = 0

        while j < len(charList):
            if (charList[i] not in stack):
                stack.append(charList[j])
                j += 1
                maxL = max(maxL, len(stack))
            else:
                stack.remove(charList[i])
                i += 1

        return max


testSol = Solution()
testSol.lengthOfLongestSubstring("abcb")