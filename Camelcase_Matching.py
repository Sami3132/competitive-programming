class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def checkMatch(pattern, query):
            i = 0

            for index, el in enumerate(query):
                if i < len(pattern) and pattern[i] == query[index]:
                    i += 1
                elif query[index].isupper():
                    return False

            return i == len(pattern)
        
        return [True if checkMatch(pattern, query) else False for query in queries]
