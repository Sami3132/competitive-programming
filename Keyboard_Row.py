class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        output = []

        for word in words:
            for row in rows:
                if all(ch.lower() in row for ch in word):
                    output.append(word)

        return output
