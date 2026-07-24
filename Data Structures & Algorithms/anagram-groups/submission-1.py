class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i=0
        res=defaultdict(list)
        for s in strs:
            arr=[0]*26
            for i in range(len(s)):
                arr[ord(s[i])-ord('a')]+=1
            res[tuple(arr)].append(s)
        return list(res.values())