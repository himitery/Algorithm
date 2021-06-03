num: int = int(input())

index: int = 2
while num != 1:
    if num % index == 0:
        num = num // index
        print(index)
    else:
        index += 1
