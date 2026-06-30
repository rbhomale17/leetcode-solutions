class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build Trie
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node['$'] = word  # mark end of word

        rows, cols = len(board), len(board[0])
        found = set()

        def dfs(r, c, parent):
            letter = board[r][c]
            curr_node = parent[letter]

            # check if word is found
            word_match = curr_node.pop('$', False)
            if word_match:
                found.add(word_match)

            board[r][c] = '#'  # mark visited

            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] in curr_node
                ):
                    dfs(nr, nc, curr_node)

            board[r][c] = letter  # backtrack

            # remove leaf nodes to prune search space
            if not curr_node:
                parent.pop(letter)

        # Step 2: Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie:
                    dfs(r, c, trie)

        return list(found)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna