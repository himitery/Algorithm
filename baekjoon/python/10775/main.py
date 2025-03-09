import sys

read = lambda: sys.stdin.readline().rstrip()


class Problem:
    def __init__(self):
        self.g, self.p = int(read()), int(read())
        self.gates = [gate for gate in range(self.g + 1)]
        self.planes = [int(read()) for _ in range(self.p)]

    def solve(self) -> None:
        print(self.find_maximum())

    def find_maximum(self) -> int:
        count = 0
        for plane in self.planes[: self.g]:
            if not self.find_gate(plane):
                return count
            count += 1

        return count

    def find_gate(self, plain: int) -> int:
        gate = self.find_root_gate(plain)
        self.gates[gate] = self.find_root_gate(gate - 1)

        return gate

    def find_root_gate(self, gate: int) -> int:
        while self.gates[gate] != gate:
            self.gates[gate] = self.gates[self.gates[gate]]
            gate = self.gates[gate]

        return gate


if __name__ == "__main__":
    Problem().solve()
