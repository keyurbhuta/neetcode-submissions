class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for word in strs:
            a=[0]*26
            for char in word:
                a[ord(char)-ord('a')]+=1
            key=tuple(a)
            if key not in seen:
                seen[key]=[]
            seen[key].append(word)
        return list(seen.values())

        
            
            
