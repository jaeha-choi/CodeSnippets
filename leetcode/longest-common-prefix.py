class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        pref = strs[0]
        for word in strs[1:]:
            if len(word) < len(pref):
                pref = pref[:len(word)]
            while pref != word[:len(pref)]:
                pref = pref[:len(pref) - 1]
        return pref
