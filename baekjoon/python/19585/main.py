import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self) -> None:
        self.c, self.n = map(int, read().split())
        self.colors = [read() for _ in range(self.c)]
        self.nicknames = [read() for _ in range(self.n)]
        self.q = int(read())
        self.teams = [read() for _ in range(self.q)]

        self.end = "__end__"

    def solve(self) -> None:
        color_trie = {}
        for color in self.colors:
            node = color_trie
            for char in color:
                node = node.setdefault(char, {})

            node[self.end] = self.end

        nickname_trie = {}
        for nickname in self.nicknames:
            node = nickname_trie
            for char in reversed(nickname):
                node = node.setdefault(char, {})

            node[self.end] = self.end

        for team in self.teams:
            is_prefix_valid, is_suffix_valid = [False] * len(team), [False] * len(team)

            node = color_trie
            for idx, char in enumerate(team):
                if char not in node:
                    break

                node = node[char]
                if self.end in node:
                    is_prefix_valid[idx] = True

            node = nickname_trie
            for idx in range(len(team) - 1, -1, -1):
                if team[idx] not in node:
                    break

                node = node[team[idx]]
                if self.end in node:
                    is_suffix_valid[idx - 1] = True

            print("Yes" if any(is_prefix_valid[idx] and is_suffix_valid[idx] for idx in range(len(team) - 1)) else "No")


if __name__ == "__main__":
    Problem().solve()
