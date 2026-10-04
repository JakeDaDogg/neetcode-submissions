class Solution:

    def encode(self, strs: List[str]) -> str:
        char = ''
        for s in strs:
            char += str(len(s)) + '#' + s
        return char

    def decode(self, s: str) -> List[str]:
        i = 0
        sol = []

        while i < len(s):
            j = i
            # extract word
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j+1
            j += length + 1
            sol.append(s[i:j])
            i = j
        return sol     
            