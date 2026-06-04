class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        store={}
        store2={}
        for letter in s:
            store[letter]=store.get(letter, 0)+1
        for letter in t:
            store2[letter]=store2.get(letter, 0)+1
        return store==store2
        