class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            res += str(length) + "!" + word 

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while s:
            idx = s.find("!")
            wordLength = int(s[0:idx])
            res.append(s[idx + 1:idx + 1 + wordLength])
            s = s[idx + 1 + wordLength:]

        # while i < len(s):
        #     print(s[i])
        #     idx = s.find("!")
        #     print(s[i:idx])
        #     wordLength = int(s[i:idx])
        #     res.append(s[idx + 1:idx + 1 + wordLength])
        #     i = idx + 1 + wordLength
        
        return res