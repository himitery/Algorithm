def solution(storey: int) -> int:
    total = 0

    while storey:
        remainder, next_digit = storey % 10, (storey // 10) % 10
        total, storey = (
            (total + 10 - remainder, storey // 10 + 1)
            if remainder > 5 or (remainder == 5 and next_digit >= 5)
            else (total + remainder, storey // 10)
        )

    return total
