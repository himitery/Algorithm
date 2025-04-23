from typing import List


def solution(expressions: List[str]) -> List[str]:
    return calculate_expression(
        list(filter(lambda x: x.split()[-1] == "X", expressions)),
        find_candidate(expressions),
    )


def find_candidate(expressions: List[str]) -> List[int]:
    bases = []
    for base in range(2, 10):
        bases.append(base)
        for expr in expressions:
            if not is_available(expr, base):
                bases.pop()
                break

    return bases


def is_available(expression: str, base: int) -> bool:
    a, op, b, _, c = expression.split()

    if not all(int(ch) < base for ch in a):
        return False
    if not all(int(ch) < base for ch in b):
        return False

    if c == "X":
        return True

    if not all(int(ch) < base for ch in c):
        return False
    if int(a, base) + int(b, base) * (1 if op == "+" else -1) != int(c, base):
        return False

    return True


def calculate_expression(expressions: List[str], bases: List[int]) -> List[str]:
    results = []
    for expression in expressions:
        a, op, b, _, c = expression.split()

        computed = {
            int_to_str(
                int(a, base) + int(b, base) * (1 if op == "+" else -1),
                base,
            )
            for base in bases
        }

        results.append(f"{a} {op} {b} = {computed.pop() if len(computed) == 1 else '?'}")

    return results


def int_to_str(num: int, base: int) -> str:
    if num == 0:
        return "0"

    digits = []
    while num > 0:
        digits.append(str(num % base))
        num //= base

    return "".join(reversed(digits))
