class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def helper(digitToChar, res, cur, pointer, digits):
            if pointer == len(digits):
                res.append("".join(cur))
                return
            for c in digitToChar[digits[pointer]]:
                cur.append(c)
                helper(digitToChar, res, cur, pointer + 1, digits)
                cur.pop()
        
        if not digits: return []
        helper(digitToChar, res, [], 0, digits)

        return res
