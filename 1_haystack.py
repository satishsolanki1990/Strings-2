class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        if len(needle) == 0:
            return 0
        # brute force
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                temp = i
                for j in range(len(needle)):
                    if needle[j] != haystack[temp]:
                        break
                    else:
                        temp += 1
                    if temp == len(haystack) and j < len(needle) - 1:
                        return -1
                if (temp - i) == len(needle):
                    return i

        return -1


