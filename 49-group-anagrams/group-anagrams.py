class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        group = {}

        for i in range(n):
            temp = sorted(strs[i])
            temp = "".join(temp)
            group.setdefault(temp, []).append(strs[i])

        return list(group.values())