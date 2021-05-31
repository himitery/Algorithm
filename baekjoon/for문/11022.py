num: int = int(input())

for i in range(1, num + 1):
    data: list() = list(map(int, input().split()))
    print(f"Case #{i}: {data[0]} + {data[1]} = {sum(data)}")
