class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memo = {}

        def solve(i, j):

            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:

                answer = solve(i + 1, j + 1)

            else:

                insert_operation = 1 + solve(i, j + 1)

                delete_operation = 1 + solve(i + 1, j)

                replace_operation = 1 + solve(i + 1, j + 1)

                answer = min(
                    insert_operation,
                    delete_operation,
                    replace_operation
                )

            memo[(i, j)] = answer

            return answer

        return solve(0, 0)
