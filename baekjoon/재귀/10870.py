num: int = int(input())

fibo: list[int] = [0, 1]
for _ in range(num - 1):
    fibo.append(sum(fibo))
    fibo = fibo[-2:]
print(fibo[-1] if num != 0 else 0)
