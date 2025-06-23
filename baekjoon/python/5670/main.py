import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.n = int(read())
        self.words = [read() for _ in range(self.n)]

    def solve(self) -> None:
        total, trie = 0, self.make_trie()
        for word in self.words:
            total += self.count_keystrokes(word, trie)

        print(f"{total / self.n:.2f}")

    def make_trie(self) -> dict:
        trie = {}

        for word in self.words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})

            node["*"] = True

        return trie

    def count_keystrokes(self, word: str, trie: dict) -> int:
        strokes, node = 1, trie[word[0]]

        for char in word[1:]:
            if len(node) > 1 or "*" in node:
                strokes += 1

            node = node[char]

        return strokes


if __name__ == "__main__":
    while True:
        try:
            Problem().solve()
        except (EOFError, ValueError):
            break
